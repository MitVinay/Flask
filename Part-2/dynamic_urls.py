from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Welcome  to the Home Page</h1>"


@app.route("/welcome/steve")
def welcome_steve():
    return "<h1>Hey steve, Welcome to our Webpage</h1>"


@app.route("/welcome/tony")
def welcome_tony():
    return "<h1>Hey Tony, Welcome to our Webpage</h1>"

"""
The above function are example of static Urls,
Below code junk is an example of dynamic Url.
"""
@app.route("/welcome/<name>")
def welcome_name(name):
    return f"<h1>Hey ,{name}, Welcome to our Webpage</h1>"


if __name__ =="__main__":
    app.run(debug=True)
