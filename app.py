from flask import Flask
from flask import request
from flask import flash, redirect
from flask import jsonify
import sys
import zipfile
import hashlib
import sqlite3
import os
import random
import string

app = Flask(__name__)

###########################################
##            CHATELAIN  NOAH            ##
##             GYRE AMBROISE             ##
##              FISA TI-2023             ##
##             TP2 WebServeur            ##
###########################################

# /!\ Nos versions de python étant supérieures à celles requises pour le TP
# Nous avons donc décidé de le programmer dans un conteneur Docker avec une version python 3.8.12
# Suivez notre README afin de deployer l'application

# Run : python3 app.py
# OU
# Suivre les étapes du README


# Fonction qui retourne un String
# Permettant de générer une chaîne de 6 caractères aléatoires
def createRandomString():
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(6))


UPLOAD_FOLDER = "fichiers_reception/"
app.config['TEMP_ZIP_FOLDER'] = './temp_zip_folder/'


@app.route('/extract', methods=["POST"])
def extract():
    if request.method == "POST":
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        file.save(os.path.join(app.config['TEMP_ZIP_FOLDER'], file.filename))

        with zipfile.ZipFile(app.config['TEMP_ZIP_FOLDER'] + file.filename, "r") as zip_ref:
            zip_ref.extractall(UPLOAD_FOLDER)
        
        for filename in os.listdir(UPLOAD_FOLDER + file.filename.split(".")[0]):
            print(os.path.join(UPLOAD_FOLDER + file.filename.split(".")[0], filename))
            sha1sum = hashlib.sha1()
            with open(os.path.join(UPLOAD_FOLDER + file.filename.split(".")[0], filename), 'rb') as source:
                block = source.read(2**16)
                while len(block) != 0:
                    sha1sum.update(block)
                    block = source.read(2**16)
            print(sha1sum.hexdigest() + "\n")

    return "OK\n"


@app.route('/bonjour')
def bonjour():
    return 'Hello World\n'


app.run(host="0.0.0.0", port=5000)
