from flask_wtf import FlaskForm
from wtforms import IntegerField, HiddenField, StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class Form(FlaskForm):
  start=IntegerField('number', validators=[DataRequired()])
  submit = SubmitField('Validate')

