from flask_wtf import FlaskForm
from wtforms import StringField,DateTimeField,IntegerField,TextField, PasswordField
from wtforms.validators import DataRequired,Email
from wtforms.fields.html5 import DateField, TimeField
from datetime import date

class UserForm(FlaskForm):
    username = StringField('Логин', validators=[DataRequired()], render_kw={"placeholder": "username"})
    email = StringField('Email', validators=[Email(), DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])


class EventForm(FlaskForm):
    title = StringField('Заголовок', validators=[DataRequired()], render_kw={"placeholder": "Заголовок"})
    description = StringField('Описание', validators=[DataRequired()], render_kw={"placeholder": "Описание"})
    date_start = DateField('Дата начала: ', validators=[DataRequired()], default=date.today)
    time_start = TimeField('Время начала', format='%H:%M', validators=[DataRequired()])
    date_end = DateField('Дата окончания', validators=[DataRequired()], default=date.today)
    time_end = TimeField('Время окончания', format='%H:%M', validators=[DataRequired()])

class LoginForm(FlaskForm):
    username = StringField('Username')
    password = PasswordField('Password')


