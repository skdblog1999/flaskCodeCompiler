from flask import Flask, render_template
from flask_socketio import SocketIO


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)


@app.route('/')
def home():
    return render_template('index.html')


@socketio.on('run_code')
def run_code(data):
    print(data)


@socketio.on('submit_code')
def submit_code(data):
    print(data)


if __name__ == '__main__':
    socketio.run(app, debug=True)
