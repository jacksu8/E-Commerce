import pyrebase
from flask import *
app = Flask(__name__)

firebaseConfig = {
    "apiKey": "AIzaSyCJsleVIbnz9cwyFEy7pmPID17_TRjEodA",
    "authDomain": "nullibuy.firebaseapp.com",
    "databaseURL": "https://nullibuy.firebaseio.com",
    "projectId": "nullibuy",
    "storageBucket": "nullibuy.appspot.com",
    "messagingSenderId": "502029943947",
    "appId": "1:502029943947:web:d669d4f507f6279919808e",
    "measurementId": "G-VNY6DV0CY1"
}

firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()

@app.route("/", methods=['GET', 'POST'])

def login():
    if request.method == 'POST':
        email = request.form['name']
        password = request.form['pass']
        auth.sign_in_with_email_and_password(email, password)
    
if __name__ == '__main__':
    app.run()
