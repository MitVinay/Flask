from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

"""
The url is the link of the database we want to use. please
refer for more information in the link below
https://flask-sqlalchemy.palletsprojects.com/en/2.x/config/

"""
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///store1.db" 
# to hide the warning etc given by SQLite, this is optional
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


db = SQLAlchemy(app)

customer_product = db.Table(
    "customer_product", db.Column("customer_id", db.Integer,
                                   db.ForeignKey("customers.id")),
                                   db.Column("product_id", db.Integer,
                                   db.ForeignKey("products.id"))

)


class Customer(db.Model):
    __tablename__ = "customers"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False )
    email = db.Column(db.String(50), nullable=False, unique=True)
    # backref represents an instance of product own by what all customer
    #  add aditonal relationship
    items = db.relationship("Product", backref="owners", secondary=customer_product)
    
    def __repr__(self):
        return f"Customer({self.name}, {self.email})"
    
class Product(db.Model):
    __tablename__ = "products"
    id = db.Column(db.Integer, primary_key=True)
    product = db.Column(db.String(50), nullable=False )
    price = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f"Product({self.product}, {self.price})"

"""
This is an Association table or Bridging table to resolve many to many 
relationship. It is table not a model that we are creating.
"""


if __name__ == "__main__":
    app.run(debug=True)