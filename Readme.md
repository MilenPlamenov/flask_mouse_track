# Mouse Movement and Webcam Capture Application

This application captures mouse movement data and allows users to capture images from a connected webcam by clicking on the web interface. The captured data (mouse coordinates and image paths) are stored in an SQLite database.

## Features

- Real-time visualization of mouse coordinates on a web interface.
- Capture images from a connected webcam by clicking on the interface.
- Store captured data (mouse coordinates and image paths) in an SQLite database.
- Web interface served using Flask with SocketIO for real-time updates.

## Technologies Used

- Python 3.x
- Flask - Web framework for Python
- Flask-SocketIO - WebSocket integration for Flask
- SQLite - Lightweight relational database
- OpenCV - Computer vision library for capturing images from webcam

## Setup Instructions

### Prerequisites

- Python 3.x installed on your system.
- Webcam connected to your computer.

### Installation and setup

1. Steps:

   ```bash
   git clone https://github.com/MilenPlamenov/flask_mouse_track.git
   cd MouseChecking
    ```

   ```bash
   python -m venv venv
   source venv/bin/activate
    ```

   ```bash
   pip install -r requirements.txt
    ```
   
   ```bash
   python app.py
    ```
