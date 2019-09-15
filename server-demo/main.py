import os
from flask import Flask,render_template

#Initialize Flask
app = Flask(__name__)

#Initialize Firebase DB
import pyrebase

config = {
  "apiKey": "AIzaSyCA64ir3rDXaer9gcExR2k2sMUuUQA_5PU",
  "authDomain": "hack-mit-2e096.firebaseapp.com",
  "databaseURL": "https://hack-mit-2e096.firebaseio.com",
  "storageBucket": "hack-mit-2e096.appspot.com",
  "serviceAccount": "hack-mit-2e096-firebase-adminsdk-u0606-f54e8a8410.json"
}
firebase = pyrebase.initialize_app(config)

@app.route('/')
def demo():
    return render_template('index.html')

@app.route('/list', methods=['GET'])
def read():
    return "hello"


if __name__ == "__main__":
    app.run(host= '0.0.0.0')
