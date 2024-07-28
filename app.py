from flask import Flask, render_template, request, redirect, url_for
from flask import session as login_session 
import pyrebase

app = Flask(__name__)
app.config['SECRET_KEY']="*******"

firebaseConfig = {
  'apiKey': "AIzaSyC8SEDSRYBW0hh3p5rk7YdWvzQcF1--zsI",
  'authDomain': "einar-case-study.firebaseapp.com",
  'projectId': "einar-case-study",
  'storageBucket': "einar-case-study.appspot.com",
  'messagingSenderId': "449189864578",
  'appId': "1:449189864578:web:6bf15a20b73355c015c09b",
  'measurementId': "G-3DLSXW8H7D",
  'databaseURL':"https://einar-case-study-default-rtdb.europe-west1.firebasedatabase.app/"
}

firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()
db = firebase.database()
storage = firebase.storage()

@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == 'GET':
        return "Hello"

if __name__ == '__main__':
    app.run(debug=True)