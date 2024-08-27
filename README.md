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

## Screenshots

| **SignUp Screen** | **SignIn Screen** |
|:---:|:---:|
| ![SignUp Screen](https://github.com/user-attachments/assets/f3c9ef2e-eb27-435d-82d0-d0e32bb03893) | ![feed_screen1](https://github.com/user-attachments/assets/527fb2f7-0cdc-424d-bc14-3cbd7aa45f25) |

| **SignIn Screen with User Input** | **Home Screen** |
|:---:|:---:|
| ![sign_in_with_id](https://github.com/user-attachments/assets/54f73a8a-888a-4bc9-bd9f-331c600f9a41) | ![home_screen](https://github.com/user-attachments/assets/6718c0c4-7ddd-4183-a3e3-cde5212393a8)


| **Home Screen** | **Home Screen** |
|:---:|:---:|
| ![home_screen_2](https://github.com/user-attachments/assets/f3fe0041-2e17-43af-afe4-97f8fbd24292) |  ![home_screen_3](https://github.com/user-attachments/assets/fbb56ccb-6be2-4778-a022-3856423b3220)


| **Upload Song** | **Upload Song Screen** |
|:---:|:---:|
| ![upload_songs](https://github.com/user-attachments/assets/fd7a44b1-ecf8-4841-a207-98629a0643e1) | ![upload_song_screen](https://github.com/user-attachments/assets/c14d5471-5d1c-4962-8d28-f0fa74f70029)


| **Upload Song** | **Upload Song with Color Picker** |
|:---:|:---:|
| ![upload_song_screen1](https://github.com/user-attachments/assets/695f6c1c-3d51-4372-ace9-b0aff689b7e4) |![upload_song2](https://github.com/user-attachments/assets/f904239b-8eaa-4467-a7a2-b1770abd8e95)



| **Song Play Screen** | **Song Play Screen** |
|:---:|:---:|
| ![song_screen](https://github.com/user-attachments/assets/2dbf71c8-dc48-4031-9ea4-e4b775faeae3) | ![song_screen1](https://github.com/user-attachments/assets/c8ab455c-bda8-4726-a46f-4d21390cb7a2)



| **Song Latest Played** | **Songs Liked** |
|:---:|:---:|
| ![song_latest_played](https://github.com/user-attachments/assets/a8d9b60f-1dfe-4b89-8ecf-f196f297a384) | ![liked_songs](https://github.com/user-attachments/assets/c8a72d3f-c990-4ab5-8746-6157e29d8ab5)
