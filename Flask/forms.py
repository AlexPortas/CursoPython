from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, EmailField, PasswordField
from wtforms.validators import DataRequired, Email, Length

class SignupForm (FlaskForm):
    name=StringField("Nombre", validators=[DataRequired(), Length(max=10)])
    password=PasswordField("Contraseña", validators=[DataRequired(), Length(min=3)])
    email=EmailField("Correo electrónico", validators=[DataRequired(), Email()])
    submit=SubmitField("Enviar")