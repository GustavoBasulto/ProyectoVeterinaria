from flask_app.controllers import core, usuarios, medicamentos, mascotas, atenciones
from flask_app import app
            
if __name__ == "__main__":
    app.run(debug=True)