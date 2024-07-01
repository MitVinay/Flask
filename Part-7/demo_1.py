from flask import (Flask,
                   render_template,
                   redirect,
                   url_for,
                   flash,
                   request,
                   make_response)
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
    user_name = request.cookies.get("user_name")
    if user_name is None:
        flash("Login Required")
        """
        Once we login in properly, then we want to come back to the
        page the user requested which is About page
        So we will store this endpoint using request.url
        """
        return redirect(url_for("login", next=request.url))
    else:
        flash(f"Hi {user_name}, have a goodday")
    return render_template("about.html", title = "About")

@app.route("/contact")
def contact():
    user_name = request.cookies.get("user_name")
    if user_name is None:
        flash("Login Required")
        """
        Once we login in properly, then we want to come back to the
        page the user requested which is Contact page
        So we will store this endpoint using request.url
        """
        return redirect(url_for("login", next=request.url))
    else:
        flash(f"Hi {user_name}, have a goodday") 

    return render_template("contact.html", title = "Contact")

# WE ARE SENDING DATA, WE NEED POST AS WELL, BY DEFAULT IS GET
@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user_name = form.username.data
        response = make_response("")
        response.set_cookie("user_name", user_name)
        flash(f"Successfully loggin in as {user_name.title()}")
        next_url = request.args.get("next") or url_for("home")
        response.headers["Location"] = next_url
        response.status_code = 302
        return response

    return render_template("login.html", title = "Login", form=form)

if __name__ == "__main__":
    app.run(debug=True)