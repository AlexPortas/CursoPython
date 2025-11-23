from flask import Flask, render_template, url_for, request, redirect
import os
from flask_sqlalchemy import SQLAlchemy
from forms import SignupForm
from flask_login import current_user, login_user, logout_user, login_required
from models import User, db, login_manager

app=Flask(__name__)

app.config["SECRET_KEY"]="lqawerellj21o44joooooooo21"
app.config["SQLALCHEMY_DATABASE_URI"]="postgresql://postgres:root@localhost:5432/webFlask"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False
db.init_app(app)
login_manager.init_app(app)
login_manager.login_view="inicia_sesion"

# @app.before_first_request
# def create_table():
#     db.create_all()
posts=[]
empleados=["Alex", "Ana", "Bea", "Eva", "Pepe"]
@app.route('/')
def saludo():
    return render_template("index.html", empleados=empleados, num_emp=len(empleados),posts=posts)

@app.route('/quienes')
@login_required
def quienes():
    return render_template("aboutus.html", empleados=empleados)

@app.route('/usuarios/<int:usu>')
def usuarios(usu):
    return render_template("usuarios/usuarios.html", usu=usu)

@app.route('/contacto', methods=["GET","POST"])
def contacta():
    form=SignupForm()

    if form.validate_on_submit():
        nombre=form.name.data
        correo=form.email.data
        pwd=form.password.data
        print("Nombre -----------------", nombre)
        print("Correo -----------------", correo)
        print("Contraseña -----------------", pwd)
        return redirect(url_for("saludo"))
    return render_template("contacto.html", form=form)

@app.route('/anhadir_post', methods=["GET","POST"])
def anhadir_post():
    global posts
    if request.method=="POST":
        titulo=request.form["titulo"]
        entrada=request.form["entrada"]
        posts.append("{} --> {}".format(titulo,entrada))

        return redirect(url_for("saludo"))
    return render_template("entrada.html")

@app.route('/login', methods=["GET","POST"])
def inicia_sesion():
    if current_user.is_authenticated:
        return redirect(url_for("saludo"))

    if request.method=="POST":
        nick=request.form["nick"]
        pwd=request.form["pwd"]

        user=User.query.filter_by(nombre=nick).first()
        if user is not None and user.check_password(pwd):
            login_user(user)
            return redirect(url_for("saludo"))
    return render_template("login.html")


@app.route('/cerrar_sesion')
def cerrar_sesion():
    logout_user()
    return redirect(url_for("saludo"))

if __name__=="__main__":
    os.environ['FLASK_ENV']="development"
    with app.app_context():
        db.create_all()
        app.run(debug=True)