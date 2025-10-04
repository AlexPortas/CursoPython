from flask import Flask, render_template, url_for
import os

app=Flask(__name__)

empleados=["Alex", "Ana", "Bea", "Eva", "Pepe"]
@app.route('/')
def saludo():
    return render_template("index.html", empleados=empleados, num_emp=len(empleados))

@app.route('/quienes')
def quienes():
    return render_template("aboutus.html", empleados=empleados)

@app.route('/usuarios/<int:usu>')
def usuarios(usu):
    return render_template("usuarios/usuarios.html", usu=usu)

if __name__=="__main__":
    os.environ['FLASK_ENV']="development"
    app.run(debug=True)