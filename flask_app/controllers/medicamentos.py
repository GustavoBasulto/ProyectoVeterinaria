import os
from flask_app.models.medicamento import Medicamento
from flask import flash, redirect, render_template, request, session
from flask_app import app

@app.route("/agregar_medicamento", methods=["POST"])
def agregar_medicamento():
    if not Medicamento.validar_descripcion(request.form):
        return redirect('/medicamentos')
    data = {
        "descripcion": request.form["descripcion"],   
    }

    Medicamento.save(data)
    flash(f"exito al agregar el medicamento", "success")
    return redirect("/medicamentos")


@app.route("/eliminar_medicamento/<id>")
def eliminar_medicamento(id):
    if 'mail' in session:
        borrar=Medicamento.delete(id)
        if  borrar==False:
            flash("Medicamento presenta atenciones","warning")
        else:
            flash("Medicamento eliminado exitosamente","success")
        return redirect("/medicamentos")
    else:
        return redirect("/")

    
@app.route("/modificar_medicamento/<id>")
def medicamento_modificar(id):
    if 'mail' in session:
        return render_template("modificar_medicamento.html", medicamento=Medicamento.get_by_id(id))
    else:
        return redirect ("/")

@app.route("/modificar/<id>/medicamento", methods=["POST"])
def modificar_medicamento(id):
    if not Medicamento.validar_descripcion(request.form):
        return redirect('/medicamentos')
    data = {
        "id" : request.form["id"],
        "descripcion": request.form["descripcion"]
    }
    Medicamento.update(data)
    flash("Medicamento modificado exitosamente","success")
    return redirect('/medicamentos')

