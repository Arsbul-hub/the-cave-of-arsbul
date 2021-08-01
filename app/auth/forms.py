from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo
from app.models import User


class LoginForm(FlaskForm):
    username = StringField('Пользователь', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    remember_me = BooleanField('Запомнить меня')
    submit = SubmitField('Вход')


class RegistrationForm(FlaskForm):
    username = StringField('Пользователь', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    password2 = PasswordField(
        'Повтор пароля', validators=[DataRequired(),
                                           EqualTo('password')])
    submit = SubmitField('Зарегистрироваться')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Такой пользователь уже есть')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Эта почта уже занята')


class ResetPasswordRequestForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Запросить сброс пароля')


class ResetPasswordForm(FlaskForm):
    password = PasswordField('Пароль', validators=[DataRequired()])
    password2 = PasswordField(
        'Повтор пароля', validators=[DataRequired(),
                                           EqualTo('password')])
    submit = SubmitField('Запросить сброс пароля')
