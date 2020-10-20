from datetime import datetime
from flask_wtf import FlaskForm
# from wtforms.fields import BooleanField, DateField, StringField, SubmitField, TextAreaField, TimeField    # this is ugly, so use below instead
from wtforms.fields import (
  BooleanField, DateField, StringField, SubmitField, TextAreaField, TimeField
)
from wtforms.validators import DataRequired, ValidationError
from wtforms.widgets.html5 import DateInput, TimeInput

class AppointmentForm(FlaskForm):
  name = StringField("Name", [DataRequired()])
  start_date = DateField("Start date", [DataRequired()], widget=DateInput())
  start_time = TimeField("Start_time", [DataRequired()], widget=TimeInput())
  end_date = DateField("End_date", [DataRequired()], widget=DateInput())
  end_time = TimeField("End_time", [DataRequired()], widget=TimeInput())
  description = TextAreaField("Description", [DataRequired()])
  private = BooleanField("Private?", [DataRequired()])
  submit = SubmitField("Create an appointment")

  def validate_end_date(self, form, field):
    start = datetime.combine(form.start_date.data, form.start_time.data)
    end = datetime.combine(field.data, form.end_time.data)
    if start >= end:
      msg = "End date/time must come after start date/time"
      raise ValidationError(msg)
    if form.start_date.data != form.end_date.data:
      msg = "End date must be the same as start date"
      raise ValidationError(msg)