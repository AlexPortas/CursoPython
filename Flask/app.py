from flask import Flask, render_template, url_for
import os

app=Flask(__name__)

empleados=["Alex", "Ana", "Bea", "Eva", "Pepe"]
@app.route('/')
def saludo():
    return render_template("index.html", empleados=len(empleados))

@app.route('/quienes')
def quienes():
    return render_template("aboutus.html", empleados=empleados)

@app.route('/usuarios/<string:usu>')
def usuarios(usu):
    return "El usuario es"+usu

if __name__=="__main__":
    os.environ['FLASK_ENV']="development"
    app.run(debug=True)