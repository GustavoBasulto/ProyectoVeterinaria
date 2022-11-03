import os
from flask import flash
from flask_app.config.mysqlconnection import connectToMySQL

class Mascota:
    def __init__( self , data ):
        self.id = data['id']
        self.nombre = data['nombre']
        self.tipo_mascota = data['tipo_mascota']
        self.sexo = data['sexo']
        self.raza = data['raza']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.dueño = data['dueño']
    def __iter__(self):
        return self

    @staticmethod
    def validar_mascota(formulario):
        valido = True
        if len(formulario['nombre_mascota']) < 2:
            flash("El nombre de la mascota debe tener al menos 2 caracteres", "error")
            valido = False
        if len(formulario['raza']) < 2:
            flash("la raza de la mascota debe tener al menos 5 caracteres", "error")
            valido = False
        return valido


    @classmethod
    def save(cls, data ):
        query = "INSERT INTO mascotas (nombre, tipo_mascota, sexo, raza, created_at, updated_at, dueño) VALUES(%(nombre)s, %(tipo_mascota)s, %(sexo)s, %(raza)s, NOW(), NOW(), %(dueño)s );"
        return connectToMySQL(os.environ.get("BBDD_NAME")).query_db( query, data )

    @classmethod
    def update(cls, data):
        query = "UPDATE mascotas SET nombre = %(nombre)s, tipo_mascota = %(tipo_mascota)s, sexo = %(sexo)s, raza = %(raza)s, updated_at = NOW(), dueño = %(dueño)s WHERE id = %(id)s;"
        return connectToMySQL(os.environ.get("BBDD_NAME")).query_db( query, data )

    @classmethod
    def get_all(cls):
        query = "select m.nombre as nombre_mascota, m.id,  m.tipo_mascota, m.raza, u.nombre, u.apellido_p from mascotas m join usuarios u where m.dueño=u.identificacion;"
        results = connectToMySQL(os.environ.get("BBDD_NAME")).query_db(query)
        mascotas = []
        for mascota in results:
            mascotas.append((mascota))
        return mascotas
    
    @classmethod
    def get_all_mascotas(cls):
        query = "select * FROM mascotas;"
        results = connectToMySQL(os.environ.get("BBDD_NAME")).query_db(query)
        mascotas = []
        for mascota in results:
            mascotas.append(cls(mascota))
        return mascotas
    
    @classmethod
    def get_by_id(cls, id):
        query = "SELECT * from mascotas where id = %(id)s;"
        data={
            'id':id
        }
        results = connectToMySQL(os.environ.get("BBDD_NAME")).query_db(query, data)
        print(results)
        if not results:
            return False
        id_data = results [0]
        return id_data
    @classmethod
    def delete(cls, id ):
        query = "DELETE from mascotas WHERE id = %(id)s;"
        data={
            'id':id
        }
        info = connectToMySQL(os.environ.get("BBDD_NAME")).query_db( query, data )
        if info==False:
            return 0
        else:
            return info
    @classmethod
    def validate_mascota(cls, data):
        is_valid = True
        if len((data['nombre_mascota'])) < 2:
            flash("Debes ingresar minino 2 caracteres en nombre de  la mascota.", "error")
            is_valid = False
        if len((data['raza'])) < 2:
            flash("Debes ingresar minino 3 letras en la raza.", "error")
            is_valid = False
       
        
        return is_valid
