from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, EmailField, PasswordField
from wtforms.validators import DataRequired, Email, Length

class SignupForm (FlaskForm):
    name=StringField("nombre", validators=[DataRequired(), Length(max=10)])
    password=PasswordField("pwd", validators=[DataRequired(), Length(min=3)])
    email=EmailField("correo", validators=[DataRequired(), Email()])
    submit=SubmitField("btnEnviar")