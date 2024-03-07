from flask import Flask, render_template, request, redirect, url_for

import db, models

app = Flask(__name__) #ponemos en app nuestro servidor web de Flask

@app.route("/")
def home():
    tareas=db.sesion.query(models.Tarea).all()
    for t in tareas:
        print(t)
    return render_template("index.html", lista_de_tareas=tareas)

@app.route("/crear-tarea", methods=["POST"])
def crear():
    tarea = models.Tarea(contenido=request.form["contenido_tarea"], completado=False)
    db.sesion.add(tarea)
    db.sesion.commit()
    return redirect(url_for("home"))

@app.route("/eliminar-tarea/<id>")
def eliminar(id):
    tarea= db.sesion.query(models.Tarea).filter_by(id_tarea=id)
    for t in tarea:
        print("Se va a eliminar ->", t)
        db.sesion.delete(t)
    db.sesion.commit()
    return redirect(url_for("home"))

@app.route("/poner-hecho-tarea/<id>")
def completador(id):
    tarea= db.sesion.query(models.Tarea).filter_by(id_tarea=id)
    for t in tarea:
        t.completado=not(t.completado)
    db.sesion.commit()
    return redirect(url_for("home"))


if __name__ == '__main__':
    app.run(debug=True)
    db.Base.metadata.create_all(db.engine)