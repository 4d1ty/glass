from dotenv import load_dotenv
import os

from flask import Flask, render_template
from flask_socketio import SocketIO

load_dotenv()

socketio = SocketIO()
app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get("SECRET_KEY", "secret!")
socketio.init_app(app)



@app.get("/")
def home():
    return render_template("index.html")

if __name__ == '__main__':
    socketio.run(app)