# pip install email-validator
# pip install flask-wtf

from flask import Flask, render_template
from forms import SignupForm, LoginForm

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", title = "Home")

@app.route("/signup")
def signup():
    form = SignupForm()
    return render_template("signup.html", title = "Sign Up")

@app.route("/login")
def login():
    form = LoginForm()
    return render_template("login.html", title = "Login")



if __name__ == "__main__":
    app.run(debug=True)