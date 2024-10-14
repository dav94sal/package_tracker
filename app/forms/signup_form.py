from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.fields import EmailField
from wtforms.validators import InputRequired


class SignupForm(FlaskForm):
    first_name = StringField("First Name", validators=[InputRequired()])
    last_name = StringField("Last Name", validators=[InputRequired()])
    email = EmailField("Email", validators=[InputRequired()])
    username = StringField("Username", validators=[InputRequired()])
    password = PasswordField("Password", validators=[InputRequired()])
    submit = SubmitField("Signup")
