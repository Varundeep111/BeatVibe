# BeatVibe 🎶

**BeatVibe** is an immersive music streaming app built with **Flutter** for Android, complemented by a powerful **FastAPI** backend. The app offers users a seamless experience to sign up, upload, and discover new music, with enhanced animations, background music playback, and secure data management through **PostgreSQL** and **Hive**.

## Features

### 🔑 Login / Signup
- **Secure Authentication**: Users can easily sign up and log in, with their credentials securely stored in **PostgreSQL**.

### 🎵 Upload Songs
- **Song Management**: Users can upload their favorite songs directly through the app. Songs are securely stored in **PostgreSQL** for efficient management.

### 🆕 Latest Songs
- **Discover New Music**: The latest songs uploaded by users are showcased prominently on the home screen, keeping users up-to-date with trending tracks.

### ⏮️ Last Played Songs
- **Quick Access**: Users' recently played songs are displayed at the top of the home screen, making it easy to revisit recent favorites.

### ❤️ Liked Songs
- **Personalized Experience**: Songs that users have liked are stored and displayed in a separate section, ensuring quick access to their favorites.

### 🎧 Background Music Playback
- **Continuous Listening**: Enjoy seamless background music playback while using other apps or when the device is locked. The music continues playing without interruptions.

### 📦 Local Storage with Hive
- **Efficient Data Management**: Leveraging **Hive** for local data storage, BeatVibe ensures fast access to user preferences, playlists, and offline functionality.

### 🎨 Smooth Animations
- **Enhanced UI/UX**: The app features smooth and responsive animations throughout the interface, providing an engaging and visually appealing user experience.

### 🔄 Offline Playback
- **Play Without Internet**: BeatVibe allows users to download songs and playlists for offline playback, utilizing **Hive** for local storage.

### 🔍 Search Functionality
- **Find Your Music**: A powerful search feature enables users to quickly find songs, artists, and playlists.

### ⚙️ FastAPI Backend
- **Custom APIs**: The backend is written using **FastAPI**, allowing for fast and efficient handling of requests. This includes user authentication, song management, and playlist handling through RESTful APIs.
- **Scalability**: **FastAPI** ensures the backend is highly performant and scalable, allowing the app to grow with more users and content.

## Technology Stack

### Frontend
- **Flutter**: For building a responsive and high-performance Android app.
- **Dart**: The programming language used with Flutter.

### Backend
- **FastAPI**: For building a fast and scalable backend API service.
- **PostgreSQL**: For secure and robust storage of user data and uploaded songs.
- **Hive**: A lightweight and fast local database for storing user preferences and offline content.

### Additional Features
- **Animations**: Integrated animations for a smooth and intuitive user experience.
- **State Management**: Efficient state management across the app for a responsive and consistent UI.

## Getting Started

### Prerequisites

- **Flutter SDK**
- **PostgreSQL** Database Setup
- **FastAPI** and Python environment
- Android Device or Emulator for testing

### Installation

1. Clone the repository:
   git clone https://github.com/98021Varundeep/beatvibe.git
   cd beatvibe

2.Install dependencies for the frontend:
     flutter pub get

3.Set up the PostgreSQL database:
 Configure your database connection in the FastAPI backend.

4.Install dependencies for the backend:
  cd server
  pip install -r requirements.txt

5.Run the FastAPI server:
   uvicorn main:app --reload

6.Run the Flutter app on an Android device or emulator:
 flutter run


## UI Previews

![Untitled (1)](https://github.com/user-attachments/assets/ddc4a70d-27f1-4c4c-82e4-b10f828b4a28)



