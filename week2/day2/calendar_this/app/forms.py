from flask_wtf import FlaskForm
# from wtforms.fields import BooleanField, DateField, StringField, SubmitField, TextAreaField, TimeField    # this is ugly, so use below instead
from wtforms.fields import (
  BooleanField, DateField, StringField, SubmitField, TextAreaField, TimeField
)
from wtforms.validators import DataRequired

class AppointmentForm(FlaskForm):
  name = StringField("Name")
  start_date = DateField("Start_date")
  start_time = TimeField("Start_time")
  end_date = DateField("End_date")
  end_time = TimeField("End_time")
  description = TextAreaField("Description")
  private = BooleanField("Private?")
  submit = SubmitField("Create an appointment")