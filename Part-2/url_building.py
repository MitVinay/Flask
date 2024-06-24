import time
from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1> Welcome to our Home Page!</h1>"

@app.route("/pass/<sname>/<int:marks>")
def passed(sname, marks):
    return f"<h1> Congratulations {sname.title()}, You have passed with {marks}!</h1>"

@app.route("/fail/<sname>/<int:marks>")
def failed(sname, marks):
    return "<h1> Sorry {sname}, You have failed with {marks}!</h1>"


@app.route("/score/<name>/<int:num>")
def score(name, num):
    if num < 30:
        # We need to redirect user to a page "fail"\
        # Redirect function is expecting a Url to redirect, either we can do it manually, but that is not a good practice
        # So to avoid the manual way, we will be using url_for
        # in this url_for we pass the function name
        time.sleep(1)
        return redirect(url_for("failed", sname=name, marks=num))
    else:
        # We need to redirect user to a page "Pass"
        time.sleep(1)
        return redirect(url_for("passed",  sname=name, marks=num))


if __name__ == "__main__":
    app.run(debug=True)