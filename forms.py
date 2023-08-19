from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, EqualTo
from markupsafe import Markup


class LoginForm(FlaskForm):
    username = StringField(
        "username", validators=[DataRequired()], render_kw={"placeholder": "Username"}
    )
    password = PasswordField(
        "password",
        validators=[DataRequired(), Length(min=8, max=20)],
        render_kw={"placeholder": "Passwords"},
    )
    submit = SubmitField("Login")


class RegistrationForm(FlaskForm):
    username = StringField(
        "username", validators=[DataRequired()], render_kw={"placeholder": "Username"}
    )
    password = PasswordField(
        "password",
        validators=[DataRequired(), Length(min=8, max=20)],
        render_kw={"placeholder": "password"},
    )
