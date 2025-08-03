from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, BooleanField, SubmitField,PasswordField
from wtforms.validators import DataRequired, Email, EqualTo,Length


class LoginForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Login")

class RegisterForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired(), Length(min=3)])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=6)])
    confirm = PasswordField("Confirm Password", validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField("Register")

class ContactForm(FlaskForm):
    requester = StringField('Requester', validators=[DataRequired(), Length(max=50)])
    subject = StringField('Subject', validators=[DataRequired(), Length(max=100)])
    description = TextAreaField('Description', validators=[DataRequired()])
    not_robot = BooleanField('I am not a robot', validators=[DataRequired()])
    submit = SubmitField('Submit')
    cancel = SubmitField('Cancel')
