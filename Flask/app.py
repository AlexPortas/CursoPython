from flask import Flask, render_template, url_for
import os

app=Flask(__name__)

empleados=["Alex", "Ana", "Bea", "Eva", "Pepe"
".0"]
@app.route('/')
def saludo():
    return render_template("index.html", empleados=len(empleados))

if __name__=="__main__":
    os.environ['FLASK_ENV']="development"
    app.run(debug=True)