from flask import Flask
import os

from Server.status import *

app = Flask(__name__)

@app.route("/", methods=["GET"])
def callstatus():
       return "running";

if __name__ == '__main__':
    app.run(debug=True)
