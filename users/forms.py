from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Email, Length, ValidationError, EqualTo

def character_check(form,field):
    excluded_chars = "<&%"

    for char in field.data:
        if char in excluded_chars:
            raise ValidationError(f"Character {char} is not allowed.")

class RegisterForm(FlaskForm):
    username = StringField(validators=[DataRequired(), Email(), character_check()])
    password = PasswordField(validators=[DataRequired(), Length(min=8, max=15), character_check()])
    confirm_password = PasswordField(validators=[EqualTo('password', message='Both password field must be equal')])
    submit = SubmitField()
