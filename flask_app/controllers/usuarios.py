import os
from flask_app.models.usuario import Usuario
from flask import flash, redirect, request, session, render_template
from flask_app import app
from flask_bcrypt import Bcrypt

bcrypt=Bcrypt(app)

@app.route("/agregar_usuario", methods=["POST"])
def agregar_usuario():
    
    if not Usuario.validate_user(request.form):
        return redirect('/administracion')

    if Usuario.get_by_mail(request.form['mail']):
        flash(f"El correo {request.form['mail']} ya esta registrado", "error")
        return redirect('/administracion')
    
    hash_pass = bcrypt.generate_password_hash(request.form['contraseña'])
    
    data = {
        "id": request.form["identificacion"],
        "nombre": request.form["nombre"],
        "apellidoP" : request.form["apellidoP"],
        "apellidoM" : request.form["apellidoM"],
        "tipo" : request.form["tipo"],
        "telefono" : request.form["telefono"],
        "mail" : request.form["mail"],
        "contraseña" : hash_pass
    }
    Usuario.save(data)
    flash(f"exito al agregar el usuario {data['nombre']}", "success")
    return redirect("/administracion")





@app.route("/modificar_usuario/<id>", methods=["POST"])
def modificar_usuario(id):
    info_user=Usuario.get_by_id(id)

    if not Usuario.validate_update(request.form):
        return redirect('/administracion')
    
    email_data=Usuario.get_by_mail(request.form['mail'])
    print(email_data)
    if email_data==False:
        print("no hay usuarios con ese correo")
    elif request.form['mail']==email_data['mail']:
        print("No quiere modificar su correo")
    else:
        flash(f"El correo {request.form['mail']} ya esta registrado", "error")
        return redirect('/administracion')
    if len(request.form['contraseña'])>1:
        hash_pass = bcrypt.generate_password_hash(request.form['contraseña'])
    else:
        hash_pass=info_user['contraseña']
    data = {
        "id": request.form["id"],
        "nombre": request.form["nombre"],
        "apellidoP" : request.form["apellidoP"],
        "apellidoM" : request.form["apellidoM"],
        "telefono" : request.form["telefono"],
        "mail" : request.form["mail"],
        "contraseña" : hash_pass
    }
    Usuario.update(data)
    flash(f"exito al modificar el usuario {data['nombre']}", "success")
    return redirect("/administracion")

@app.route("/eliminar/<id>")
def eliminar_usuario(id):
    
    if 'mail' in session:
        borrar=Usuario.delete(id)
        if  borrar==False:
            flash("Usuario presenta atenciones","warning")
        else:
            flash("Usuario eliminado exitosamente","success")
        return redirect("/administracion")
    else:
        return redirect("/")


@app.route("/usuarios/<id>/modificar")
def usuario_modificar(id):
    if 'mail' in session:
        return render_template("modificar_usuario.html", usuario=Usuario.get_by_id(id))
    else:
        return redirect ("/")
   
