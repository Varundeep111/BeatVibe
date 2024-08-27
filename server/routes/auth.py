
import uuid
import bcrypt
from fastapi import Depends, HTTPException, Header
from database import SessionLocal
from middleware.auth_middleware import auth_middleware
from models.user import User
from pydantic_schemas.user_create import UserCreate
from fastapi import APIRouter   
from database import get_db 
from sqlalchemy.orm import Session
import jwt;
from pydantic_schemas.user_login import UserLogin
from sqlalchemy.orm import joinedload 

router = APIRouter()

@router.post('/signup' , status_code =  201)
def signup_user(user: UserCreate , db:Session = Depends(get_db)):
    try:
        # Check if user already exists
        user_db = db.query(User).filter(User.email == user.email).first()
        
        if user_db:
            raise HTTPException(status_code=400, detail='User with the same email ID already exists!')
        
        # Hash the password
        hashed_pw = bcrypt.hashpw(user.password.encode(), bcrypt.gensalt())
        
        # Create a new User object and add it to the session
        new_user = User(id=str(uuid.uuid4()), email=user.email, password=hashed_pw, name=user.name)
        db.add(new_user)
        
        # Commit the transaction
        db.commit()
        
        # Optionally refresh the user object
        db.refresh(new_user)
        
        return  new_user
        
    except Exception as e:
        # Handle any exceptions and rollback the transaction
        db.rollback()
        raise HTTPException(status_code=400, detail=str(e))
    
    finally:
        # Ensure the session is always closed
        db.close()


@router.post('/login')
def login_user(user: UserLogin,db:Session = Depends(get_db)):
    user_db  =  db.query(User).filter(User.email == user.email).first()
     
    if not user_db:
        raise HTTPException(400,'USer with this email   does not Exists!')
    
    
    is_match = bcrypt.checkpw(user.password.encode(), user_db.password) 
     
    if not  is_match :
         raise  HTTPException(400,"Incorrect password")
    
    token = jwt.encode({'id': user_db.id},'password_key',algorithm='HS256') 
    return {'token': token , 'user':user_db }



@router.get('/')
def current_user_data(db:Session = Depends(get_db ),
                    user_dict = Depends(auth_middleware)):
    user = db.query(User).filter(User.id ==  user_dict['uid']).options(
        joinedload(User.favorites))
          
    
    if not user:
        raise HTTPException(404, "User not found!")     


    return user    
    