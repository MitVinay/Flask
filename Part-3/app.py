from flask import Flask, render_template
from employees import employees_data

app = Flask(__name__)


# Home page
# Example on how to invoke html file
# @app.route("/")
# @app.route("/home")
# def home():
#     return render_template("home1.html")

# About Page
# @app.route("/about")
# def about():
#     return render_template("about1.html")

"""
Jinja
Concept: Parameters and Placeholders
Placeholders ={{<variable_name>}}
Paramters: Whatever passed in the render_template
"""
# @app.route("/")
# @app.route("/home")
# def home():
#     return render_template("layout.html", title="HomePage")

# @app.route("/about")
# def about():
#     return render_template("layout.html", title="Aboutpage")

"""
Jinja
Concept: Template Inheritance, block
Template Inheritance: home.html and about.html will inherit the code of
layout.html
Block : {% block content %}
"""
# Home Page
@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", title = "HomePg")

# About Page
@app.route("/about")
def about():
    return render_template("about.html", title = "AboutPg")

"""
Objective : check even or odd
Concept: If Else condition with Jinja
"""
@app.route("/evaluate/<int:num>")
def evaluate(num):
    return render_template("evaluate.html", title = "Evaluate",
                           number = num)

"""
Objective : To display the information of employees
Concept : Loop using Jinja
"""
@app.route("/employees")
def employees():
    return render_template("employees.html", title = "Employees",
                           employees = employees_data)

@app.route("/managers")
def managers():
    return render_template("managers.html", title = "Managers",
                           mangrs = employees_data)


if __name__ == "__main__":
    app.run(debug=True)

