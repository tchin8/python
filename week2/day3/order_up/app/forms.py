from flask_wtf import FlaskForm
from wtforms.fields import (
    BooleanField, DateField, StringField, SubmitField, TextAreaField, TimeField, PasswordField
)
from wtforms.validators import DataRequired, ValidationError

class LoginForm(FlaskForm):
  employee_number = StringField("Employee number", [DataRequired()])
  password = PasswordField("Password", [DataRequired()])
  submit = SubmitField("Login")