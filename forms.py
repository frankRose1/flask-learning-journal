from flask_wtf import FlaskForm
from wtforms import StringField, DateField, TextAreaField
from wtforms.validators import DataRequired, Regexp


class NewEntryForm(FlaskForm):
    title = StringField(
        'Title',
        validators=[
            DataRequired(),
            Regexp(
                r'^[a-zA-Z0-9_]*$',
                message='Letters, numbers, and underscores only!'
            )
        ])
    date = DateField(
        'Date',
        validators=[
            DataRequired()
        ],
        format='%Y-%m-%d'
    )
    time_spent = StringField(
        'Time Spent',
        validators=[
            DataRequired()
        ])
    what_i_learned = TextAreaField(
        'What I learned',
        validators=[
            DataRequired()
        ])
    resources_to_remember = TextAreaField(
        'Resources to remember',
        validators=[
            DataRequired()
        ])
