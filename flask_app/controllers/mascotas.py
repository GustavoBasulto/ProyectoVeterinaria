import imp
import os
from flask_app.models.mascota import Mascota
from flask_app.models.usuario import Usuario
from flask import flash, redirect, render_template, request, session
from flask_app import app

@app.route("/agregar_mascota", methods=["POST"])
def agregar_mascota():
    
    if not Mascota.validar_mascota(request.form):
        return redirect('/mascotas')
    data = {
        "nombre": request.form["nombre_mascota"],
        "tipo_mascota" : request.form["tipo_mascota"],
        "sexo" : request.form["sexo"],
        "raza" : request.form["raza"],
        "dueño" : request.form["dueño"]
    }
    Mascota.save(data)
    flash(f"exito al agregar la mascota {data['nombre']}", "success")
    return redirect("/mascotas")

@app.route("/eliminar_mascota/<id>")
def eliminar_mascota(id):
    
    if 'mail' in session:
        borrar=Mascota.delete(id)
        if  borrar==False:
            flash("Mascota presenta atenciones","warning")
        else:
            flash("Mascota eliminada exitosamente","success")
        return redirect("/mascotas")
    else:
        return redirect("/")

@app.route("/mascotas/<id>/modificar")
def mascota_modificar(id):
    if 'mail' in session:
        dueños=Usuario.get_by_tipo(3)
        return render_template("modificar_mascota.html", mascota=Mascota.get_by_id(id), dueños=dueños)
    else:
        return redirect ("/")


@app.route("/modificar_mascota/<id>", methods=["POST"])
def modificar_mascota(id):
    if not Mascota.validate_mascota(request.form):
        return redirect('/mascotas')
    data = {
        "id" : request.form["id"],
        "nombre": request.form["nombre_mascota"],
        "tipo_mascota": request.form["tipo_mascota"],
        "sexo": request.form["sexo"],
        "raza": request.form["raza"],
        "dueño": request.form["dueño"]

    }
    Mascota.update(data)
    flash("Mascota modificada exitosamente","success")
    return redirect('/mascotas')