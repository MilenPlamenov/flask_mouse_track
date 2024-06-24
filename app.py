from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit
import threading
import cv2
import sqlite3
import os
from datetime import datetime


app = Flask(__name__)
socketio = SocketIO(app)
os.makedirs('capture/images', exist_ok=True)


def setup_database():
    conn = sqlite3.connect('database/database.db', check_same_thread=False)
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS mouse_data (
                        id INTEGER PRIMARY KEY,
                        x INTEGER,
                        y INTEGER,
                        image_path TEXT,
                        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP)''')
    conn.commit()
    return conn, cursor


conn, cursor = setup_database()


def save_to_db(x, y, image_path):
    cursor.execute('INSERT INTO mouse_data (x, y, image_path) VALUES (?, ?, ?)', (x, y, image_path))
    conn.commit()


def capture_image(x, y):
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    if ret:
        timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
        image_path = f'capture/images/{timestamp}.jpg'
        cv2.imwrite(image_path, frame)
        save_to_db(x, y, image_path)
    cap.release()


@app.route('/')
def index():
    return render_template('index.html')


@socketio.on('mouse_move')
def handle_mouse_move(data):
    x = data['x']
    y = data['y']
    emit('update_position', {'x': x, 'y': y}, broadcast=True)


@socketio.on('mouse_click')
def handle_mouse_click(data):
    x = data['x']
    y = data['y']
    threading.Thread(target=capture_image, args=(x, y)).start()


if __name__ == '__main__':
    socketio.run(app, debug=True)
