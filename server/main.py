from models.base import Base
from routes import auth
from fastapi import FastAPI
from database import engine
from routes  import song
app = FastAPI()

app.include_router(auth.router, prefix ='/auth')
app.include_router(song.router,prefix ='/song')
# Create tables in the database
Base.metadata.create_all(engine)

# Define the UserCreate schema
