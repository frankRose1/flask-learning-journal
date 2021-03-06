from flask_wtf import FlaskForm
from wtforms.fields import StringField, TextAreaField, PasswordField
from wtforms.fields.html5 import DateField
from wtforms.validators import Regexp, required, ValidationError, length, Email, EqualTo

from models import User


def unique_username(form, field):
    if User.select().where(User.username == field.data).exists():
        raise ValidationError('That username is already taken!')


def unique_email(form, field):
    if User.select().where(User.email == field.data).exists():
        raise ValidationError('A user with that email address already exists!')


class JournalEntryForm(FlaskForm):
    title = StringField(
        'Title',
        validators=[
            required(),
        ])
    date = DateField(
        'Date',
        validators=[
            required()
        ],
        format='%Y-%m-%d'
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
            unique_email
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
