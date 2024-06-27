from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

"""
The url is the link of the database we want to use. please
refer for more information in the link below
https://flask-sqlalchemy.palletsprojects.com/en/2.x/config/

"""
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///ipl.db" 
# to hide the warning etc given by SQLite, this is optional
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


db = SQLAlchemy(app)

class Team(db.Model):

    """By default SQLAlchemy make the name of the table 
    by the name of the class name in lowercase. We can Customise or own name 
    using __tablename__
    """
    __tablename__ = "teams"
    id = db.Column(db.Integer, primary_key=True)
    team = db.Column(db.String(50), nullable=False, unique=True)
    state = db.Column(db.String(50), nullable=False)
    # this member is not a column, backref= team will 
    # create an imaginary column name team in player column and store instance of the Team table
    members = db.relationship("Player", backref="team")

    def __repr__(self):
        return f"Team({self.team}, {self.state})"

class Player(db.Model):
    __tablename__ = "players"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    nationality = db.Column(db.String(50), nullable=False)
    team_id = db.Column(db.Integer, db.ForeignKey("teams.id"))
    
    def __repr__(self):
        return f"Player({self.name}, {self.nationality})"
    


if __name__ == "__main__":
    app.run(debug=True)


