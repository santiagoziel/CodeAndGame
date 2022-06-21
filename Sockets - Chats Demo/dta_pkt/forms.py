from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, ValidationError

class RegisterForm(FlaskForm):
    username = StringField(id ="usernameID", validators=[InputRequired()], render_kw={"placeholder":"Nombre de Usuario"})
    submit = SubmitField("Ingresar")
