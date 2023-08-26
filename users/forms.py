from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Email, Length, ValidationError, EqualTo
import re

def validate_data(self, data_field):
    p = re.compile("^(?=.*\d)(?=.*[a-z])\w+$")
    if not p.match(data_field.data):
        raise ValidationError("Must contain at least 1 digit and 1 lowercase character")

def character_check(form,field):
    excluded_chars = "<&%"

    for char in field.data:
        if char in excluded_chars:
            raise ValidationError(f"Character {char} is not allowed.")

class RegisterForm(FlaskForm):
    username = StringField(validators=[DataRequired(), Email(), character_check])
    password = PasswordField(validators=[DataRequired(), Length(min=8, max=15), character_check])
    confirm_password = PasswordField(validators=[DataRequired(), EqualTo('password', message='Both password field must be equal')])
    submit = SubmitField()
