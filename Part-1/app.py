from flask import Flask

# python assign each name to the modue, module which is .py file
app  = Flask(__name__)

"""
name of the Flask object
"/" means home page
app.route means creating an endpoint.
The entire syntax below means if somebody visits the endpoint then the home
function will be called.
For the same function, we can have multiple route
"""
@app.route("/")
@app.route("/home")
def home():
    return "<h1>Welcome to the Home Page! </h1>"

# How to add a path paramter , <> 
# title() capatilaise
@app.route("/welcome/<name>")
def welcome(name):
    return f"Hi {name.title()} , you are welcome in this page"

"""
By default the input is in String,
How to define a input
"""
@app.route("/addition/<int:num>")
def addition(num):
    return f" Input is  {num}, output{num*100}" 

"""
How to take two inputs
"""
@app.route("/addition_two/<int:num1>/<int:num2>")
def addition_two(num1, num2):
    return f"<h1>Inputs are {num1, num2}, Addition will be{num1+num2}</h1>" 

#about page
@app.route("/about")
def about():
    return "<h1>Welcome to the About Page! </h1>"

if __name__ == "__main__":
    """
    debug  =  True give us the log as weel. This helps to
    analyse at the time of problem.
    """
    app.run(debug = True)
