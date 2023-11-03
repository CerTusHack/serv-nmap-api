from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
import subprocess

#configrarproyecto
app = Flask(_name_)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/')
def correr():
        try:
                texto='192.168.1.2'#puedes hacer que el ponga la ip automatica 
          #la salida es verbose tu puedes mejorarla la idea es que se corriera por una api para que lo tomase una aplicacion movil 
                salida = subprocess.check_output(['nmap', '-v', texto], universal_newlines=True)


                return jsonify([{'result': salida}]), 200
        except subprocess.CalledProcessError as e:
                return jsonify({'error': str(e)}), 500


if _name_ == '_main_':
        app.run()
