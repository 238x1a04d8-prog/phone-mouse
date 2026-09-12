from flask import Flask, render_template
from flask_socketio import SocketIO
import pyautogui

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")


@socketio.on("mouse_move")
def mouse_move(data):
    dx = data.get("dx", 0)
    dy = data.get("dy", 0)

    pyautogui.moveRel(dx, dy)


@socketio.on("left_click")
def left_click():
    pyautogui.click()


@socketio.on("right_click")
def right_click():
    pyautogui.rightClick()


@app.route("/")
def home():
    return render_template("index.html")


if __name__ == "__main__":
    print("Phone Mouse Server Started!")
    socketio.run(app, host="0.0.0.0", port=5000, debug=True)
    