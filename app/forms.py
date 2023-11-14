from flask_login import UserMixin
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, DateField
from wtforms.validators import DataRequired, Email, Length


class LoginForm(FlaskForm):
    login = StringField('login', validators=[DataRequired()],
                        render_kw={"class": "loginForm__wrapper__input", "placeholder": "Логин"})
    password = PasswordField('password', validators=[DataRequired(), Length(min=8)],
                             render_kw={"class": "loginForm__wrapper__input", "placeholder": "Пароль"})

class RegistrationForm(FlaskForm):
    login = StringField('login', validators=[DataRequired()],
                        render_kw={"class": "loginForm__wrapper__input", "placeholder": "Логин"})
    password = PasswordField('password', validators=[DataRequired(), Length(min=8)],
                             render_kw={"class": "loginForm__wrapper__input", "placeholder": "Пароль"})
    email = StringField('email', validators=[DataRequired(), Email()], render_kw={"class": "loginForm__wrapper__input", "placeholder": "Email"})