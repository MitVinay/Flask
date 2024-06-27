from flask import (Flask,
                   render_template,
                   redirect,
                   url_for,
                   flash,
                   session,
                   request)
"""
session is nothing more than a dictionary,
We will use this session in the form of dictionary,
name of the key the user_name
"""
from form import LoginForm

app = Flask(__name__)

# CSRF token is required to use WTF FORMS.
app.config["SECRET_KEY"] = "this_is_a_secret_key"

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", title = "Home")

@app.route("/about")
def about():
    if "user_name" not in session:
        flash("Login Required")
        """
        Once we login in properly, then we want to come back to the
        page the user requested which is About page
        So we will store this endpoint using request.url
        """
        return redirect(url_for("login", next=request.url))
    else:
        flash(f"Hi {session['user_name']}, have a goodday")
    return render_template("about.html", title = "About")

@app.route("/contact")
def contact():
    if "user_name" not in session:
        flash("Login Required")
        """
        Once we login in properly, then we want to come back to the
        page the user requested which is Contact page
        So we will store this endpoint using request.url
        """
        return redirect(url_for("login", next=request.url))
    else:
        flash(f"Hi {session['user_name']}, have a goodday") 

    return render_template("contact.html", title = "Contact")

# WE ARE SENDING DATA, WE NEED POST AS WELL, BY DEFAULT IS GET
@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        session['user_name'] = form.username.data 
        flash(f"Successfully loggin in as {session['user_name'].title()}")
        next_url = request.args.get("next")
        """
        If the login page is requested from a About or Contact
        the url will be stored in the next_url other wise if it is none
        the it will go back to home page
        """
        return redirect(next_url or url_for("home"))

    return render_template("login.html", title = "Login", form=form)

if __name__ == "__main__":
    app.run(debug=True)