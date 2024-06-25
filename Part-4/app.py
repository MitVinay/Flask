# pip install email-validator
# pip install flask-wtf

from flask import Flask, render_template, redirect, url_for, flash
from forms import SignupForm, LoginForm

app = Flask(__name__)

# CSRF token is required to use WTF FORMS.
app.config["SECRET_KEY"] = "this_is_a_secret_key"

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", title = "Home")

"""
As we mentioned method in signup page, We need to mention 
the method over this end point as well which is post.
By default the request is GET so we will include that so that we can come
back to the weboage. On post the data will be stored.

When an not validated input will be input by the user, it will be 
checked but we need to display the reason what went wrong.
"""
@app.route("/signup", methods = ["GET", "POST"])
def signup():
    # We will create the object of the Class and pass it as paramter in RenderTemplate
    form = SignupForm()
    if form.validate_on_submit():
        """If everything this good, this should redirect to hom page
        Flask allows you flash a message using Flash funtion"""
        flash(f"Successfully Registered {form.username.data}")
        return redirect(url_for("home"))
    return render_template("signup.html", title = "Sign Up", form = form)

@app.route("/login", methods = ["GET", "POST"])
def login():
    form = LoginForm()
    email = form.email.data
    pw = form.password.data

    if form.validate_on_submit():
        if email == "a@b.com" and pw == "12345":
            flash("User Successfully logged in.")
            return redirect(url_for("home"))

    return render_template("login.html", title = "Login", form = form)


if __name__ == "__main__":
    app.run(debug=True)