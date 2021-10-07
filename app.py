from flask import Flask
from flask import request
from flask import flash, redirect
from flask import jsonify
import json
import sys
import zipfile
import hashlib
import sqlite3
import os
import random
import string
from datetime import date

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

def checkIfFileExistInDatabase(filename):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    oneRecord = [filename]
    cursor.execute("SELECT * FROM files WHERE filename = ?", oneRecord)
    rows = cursor.fetchall()
    return len(rows) > 0

UPLOAD_FOLDER = "fichiers_reception/"
app.config['TEMP_ZIP_FOLDER'] = './temp_zip_folder/'


@app.route('/extract', methods=["POST"])
def extract():
    #Création du fichier zip avec les fichiers aux mauvais code SHA-1
    zipObj = zipfile.ZipFile('log_error_sha1_code_files.zip', 'w')
    if request.method == "POST":
        jsonCodes = json.loads(request.form["json"])
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
        
        #Remove the .DS_Store and __MACOSX files for macOS
        os.remove(UPLOAD_FOLDER + file.filename.split(".")[0] + "/.DS_Store")
        os.rmdir(UPLOAD_FOLDER + "__MACOSX")
        for index, filename in enumerate(os.listdir(UPLOAD_FOLDER + file.filename.split(".")[0])):
            try:
                index += 1
                sha1sum = hashlib.sha1()
                with open(os.path.join(UPLOAD_FOLDER + file.filename.split(".")[0], filename), 'rb') as source:
                    block = source.read(2**16)
                    while len(block) != 0:
                        sha1sum.update(block)
                        block = source.read(2**16)
                print("\nphoto" + str(index), os.path.join(UPLOAD_FOLDER + file.filename.split(".")[0], filename), sha1sum.hexdigest())
                if checkIfFileExistInDatabase(filename) == False:
                    conn = sqlite3.connect('database.db')
                    cursor = conn.cursor()
                    oneRecord = [filename, sha1sum.hexdigest(), str(date.today().strftime("%d/%m/%Y")), bool(jsonCodes["photo" + str(index)] == sha1sum.hexdigest())]
                    cursor.execute('INSERT INTO files(filename, sha1, validation_date, isOk) VALUES (?,?,?,?)', oneRecord)
                    conn.commit()
                    conn.close()
                if jsonCodes["photo" + str(index)] == sha1sum.hexdigest():
                    print("✅", filename, "SHA-1 Code is OK")
                else:
                    print("❌", filename, "SHA-1 Code is not OK ! File is added to log_error_sha1_code_files.zip")
                    zipObj.write(os.path.join(UPLOAD_FOLDER + file.filename.split(".")[0], filename))
                    os.remove(os.path.join(UPLOAD_FOLDER + file.filename.split(".")[0], filename))
            except:
                break
        print('\n')
        zipObj.close()
    return "OK\n"


@app.route('/bonjour')
def bonjour():
    return 'Hello World\n'


app.run(host="0.0.0.0", port=5000)
