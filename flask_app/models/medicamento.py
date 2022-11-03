import os
from flask import flash
from flask_app.config.mysqlconnection import connectToMySQL

class Medicamento:
    def __init__( self , data ):
        self.id = data['id']
        self.descripcion = data['descripcion']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    def __iter__(self):
        return self

    @staticmethod
    def validar_descripcion(formulario):
        valido = True
        if len(formulario['descripcion']) < 5:
            flash("tu descripcion debe tener al menos 5 caracteres", "error")
            valido = False
        return valido


    @classmethod
    def save(cls, data ):
        query = "INSERT INTO Medicamentos( descripcion, created_at, updated_at) VALUES( %(descripcion)s, NOW(), NOW() );"
        return connectToMySQL(os.environ.get("BBDD_NAME")).query_db( query, data )

    @classmethod
    def update(cls, data):
        query = "UPDATE Medicamentos SET descripcion = %(descripcion)s, updated_at = NOW() WHERE id = %(id)s;"
        return connectToMySQL(os.environ.get("BBDD_NAME")).query_db( query, data )

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM Medicamentos;"
        results = connectToMySQL(os.environ.get("BBDD_NAME")).query_db(query)
        medicamentos = []
        for medicamento in results:  
            medicamentos.append(cls(medicamento))
        return medicamentos

    @classmethod
    def delete(cls, id ):
        query = "DELETE from medicamentos WHERE id = %(id)s;"
        data={
            'id':id
        }
        info=connectToMySQL(os.environ.get("BBDD_NAME")).query_db( query, data )
        if info==False:
            return 0
        else:
            return info
    
    @classmethod
    def get_by_id(cls, id):
        query = "SELECT * from medicamentos where id = %(id)s;"
        data={
            'id':id
        }
        results = connectToMySQL(os.environ.get("BBDD_NAME")).query_db(query, data)
        if not results:
            return False
        id_data = results [0]
        return id_data