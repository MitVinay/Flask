from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

"""
The url is the link of the database we want to use. please
refer for more information in the link below
https://flask-sqlalchemy.palletsprojects.com/en/2.x/config/

"""
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///employees_db.db" 
# to hide the warning etc given by SQLite, this is optional
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


db = SQLAlchemy(app)

"""
Lets define a Table employee,
db.Model is passed to defined it as table
"""
"""
This is the builtin method of the class, So we are modifying  the 
output.
Intially if we just run class it displays its memory location with the
given below we are improving the ouput.

Using SQLAlchemy, We use model to create table in database.
"""

class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    email = db.Column(db.String(50), nullable=False, unique=True)

    def __repr__(self):
        return f"Employee({self.name}, {self.age}, {self.email})"

if __name__ == "__main__":
    app.run(debug=True)

