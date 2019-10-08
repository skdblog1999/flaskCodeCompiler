from flask import Flask, render_template
from flask_socketio import SocketIO
import database_functions as db_fun


app = Flask(__name__)
app.config["SECRET_KEY"] = "secret!"
socketio = SocketIO(app)
algo = 0


@app.route("/<int:algoID>")
def home(algoID):
    global algo
    algo = db_fun.algo_info(algoID)
    return render_template("index.html")


@socketio.on("run_code")
def run_code(data):
    global algo
    algo.put_data(data)
    print(data)


@socketio.on("submit_code")
def submit_code(data):
    print(data)


if __name__ == "__main__":
    socketio.run(app, debug=True)
