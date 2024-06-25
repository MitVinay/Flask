from flask_wtf import FlaskForm
from wtforms import (StringField, SelectField, DateField,
                      PasswordField, SubmitField,
                      BooleanField)
from wtforms.validators import (DataRequired,
                                Length,
                                Email,
                                Optional,
                                EqualTo)

class SignupForm(FlaskForm):
    """
    Username checks
    1. The field is empty or not
    2. Length of the value should be more than resitricted
    validators: 
    1. DataRequired can be used to check wether 
    the field is empty or not, in paramters 
    we can pass a message as well.
    2. To Handle the length checks, We will use the Length validator
    """
    username = StringField(label="Username",
                           validators=[DataRequired(),
                                       Length(min=2, max=30)])
    
    """
    Email checks
    1. The field is empty or not
    2. The Email should be in the right format.
    validators: 
    1. DataRequired can be used to check wether 
    the field is empty or not, in paramters 
    we can pass a message as well.
    2. To check wether email is in the right format,  
    We need Email validator
    """
    email = StringField(label="Email",
                        validators=[DataRequired(),
                                   Email() ])
    
    """
    Gender
    To take the gender input, We will provide options and user will select
    To enable that we will use SelectField.
    We wont force the user to provide the gender data, Hence to make it 
    optional We will use Optional validator.

    """
    gender = SelectField(label="Gender",
                         choices=["Male", "Female", "other"],
                         validators=[Optional()])
    

    """
    DOB

    To take the DoB input we will be using DateField

    """
    dob = DateField(label="Date of Birth", 
                    validators=[Optional()])
    
    """
    Password:
    PasswordField is used to avoid seeing the value input by the user,
    DataRequired will be used to ensure the compulsory input.
    Lastly the confirm password should be exactly same as password, 
    To enusre that We will use EqualTo validator


    """
    password = PasswordField(label="Password",
                             validators=[DataRequired(),
                                         Length(min=5, max=25)])
    
    confirm_password = PasswordField(label="Confirm Password",
                             validators=[DataRequired(),
                                         Length(min=5, max=25),
                                          EqualTo("password") ])

    submit = SubmitField("Sign Up")


class LoginForm(FlaskForm):
        
    email = StringField(label="Email",
                    validators=[DataRequired(),
                                Email() ])

    password = PasswordField(label="Password",
                             validators=[DataRequired(),
                                         Length(min=5, max=25)])

    remember_me = BooleanField("Remember Me")

    submit = SubmitField("LogIn")