import os
from flask_app.models.atencion import Atencion
from flask_app.models.medicamento import Medicamento
from flask_app.models.mascota import Mascota
from flask import flash, redirect, render_template, request, session
from flask_app import app


@app.route("/agregar_atencion", methods=["POST"])
def agregar_atencion():
    
    data = {
        "fecha": request.form['fecha'],
        "veterinario" : request.form['veterinario'],
        "mascota" : request.form['mascota'],
        "tratamiento" : request.form['tratamiento'],
        "medicamento" : request.form['medicamento']
    }
    print(data)
    Atencion.save(data)
    flash("exito al agregar la atencion", "success")
    return redirect("/atenciones")

@app.route("/eliminar_atencion/<id>")
def eliminar_atencion(id):
    if 'mail' in session:
        print(id)
        Atencion.delete(id)
        flash("Atencion eliminada exitosamente","success")
        return redirect("/atenciones")
    else:
        return redirect("/")

@app.route("/atencion/<id>/modificar")
def atencion_modificar(id):
    if 'mail' in session:
        atencion=Atencion.get_all_by_id(id)
        medicamentos=Medicamento.get_all()
        mascotas=Mascota.get_all_mascotas()
        print(atencion)
        return render_template("modificar_atencion.html", atencion=atencion, medicamentos=medicamentos, mascotas=mascotas)
    else:
        return redirect ("/")


@app.route("/modificar_atencion/<id>", methods=["POST"])
def modificar_atencion(id):
    if 'mail' in session:
        if not Atencion.validate_atencion_modificar(request.form):
            return redirect('/atencion/<id>/modificar')
        data = {
        "id": request.form['id'],
        "fecha": request.form['fecha'],
        "mascota" : request.form['mascota'],
        "tratamiento" : request.form['tratamiento'],
        "medicamento" : request.form['medicamento']
        }
        Atencion.update(data)
        flash("exito al modificar la atencion", "success")
        return redirect("/atenciones")
        
    else:
        return redirect ("/")