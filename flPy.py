from flask import Flask, render_template, request, jsonify
from hpScrapy import iniciarCodigo
import datetime

import os
app = Flask(__name__)

# Variable para almacenar el archivo CSV
uploaded_csv = None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    global uploaded_csv

    # Verifica si se envió un archivo CSV
    if 'csv_file' in request.files:
        csv_file = request.files['csv_file']
        
         # Save the file to a temporary location
        file_path = os.path.join(csv_file.filename)
        csv_file.save(file_path)

        # Almacena el archivo en la variable
        uploaded_csv = file_path
        
        # Decide the value for 'isFile' based on your logic
        is_file = True

        result = iniciarCodigo(is_file, None, file_path)

        # Devuelve una respuesta en formato JSON
        return jsonify(result)

    return "No se proporcionó un archivo CSV."

if __name__ == '__main__':
    app.run(debug=True)
