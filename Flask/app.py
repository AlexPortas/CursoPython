from flask import Flask, render_template, url_for, request, redirect
import os

from forms import SignupForm

app=Flask(__name__)

app.config["SECRET_KEY"]="lqawerellj21o44joooooooo21"
posts=[]
empleados=["Alex", "Ana", "Bea", "Eva", "Pepe"]
@app.route('/')
def saludo():
    return render_template("index.html", empleados=empleados, num_emp=len(empleados),posts=posts)

@app.route('/quienes')
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
    if request.method=="POST":
        nick=request.form["nick"]
        pwd=request.form["pwd"]
        print(nick," --> ",pwd)

        return redirect(url_for("saludo"))
    return render_template("login.html")

if __name__=="__main__":
    os.environ['FLASK_ENV']="development"
    app.run(debug=True)