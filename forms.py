from datetime import datetime

from flask_wtf import FlaskForm
from wtforms.fields import StringField, DateField, TextAreaField, PasswordField
from wtforms.validators import Regexp, required, ValidationError, length, Email, EqualTo

from models import User


def check_date_format(form, field):
    try:
        datetime.strptime(field.data, '%d/%m/%Y')
    except ValueError:
        raise ValidationError('Please use DD/MM/YYYY format')


def unique_username(form, field):
    if User.select().where(User.username == field.data).exists():
        raise ValidationError('That username is already taken!')


def unique_email(form, field):
    if User.select().where(User.username == field.data).exists():
        raise ValidationError('A user with that email address already exists!')


class NewEntryForm(FlaskForm):
    title = StringField(
        'Title',
        validators=[
            required(),
        ])
    date = DateField(
        'Date DD/MM/YYYY',
        validators=[
            required(),
            check_date_format
        ]
    )
    time_spent = StringField(
        'Time Spent',
        validators=[
            required()
        ])
    what_i_learned = TextAreaField(
        'What I learned',
        validators=[
            required()
        ])
    resources_to_remember = TextAreaField(
        'Resources to remember',
        validators=[
            required()
        ])


class RegisterForm(FlaskForm):
    username = StringField(
        'Username',
        validators=[
            required(),
            Regexp(
                r'^[a-zA-Z0-9_]*$',
                message='Username must be one word, letters, numbers, and underscores only!'
            ),
            unique_username
        ]
    )
    email = StringField(
        'Email',
        validators=[
            required(),
            Email(message='Please provide a valid email.'),
            unique_email()
        ]
    )
    password = PasswordField(
        'Password',
        validators=[
            required(),
            length(min=8, max=100),
            EqualTo('password2', message='Passwords must match!')
        ]
    )
    password2 = PasswordField(
        'Confirm Password',
        validators=[required()]
    )


class LoginForm(FlaskForm):
    email = StringField(
        'Email',
        validators=[
            required(),
            Email()
        ])
    password = PasswordField(
        'Password',
        validators=[
            required()
        ])
