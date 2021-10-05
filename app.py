from flask import Flask
from flask import request
from flask import flash, redirect
from flask import jsonify
import sqlite3
import os
import random
import string
import hashlib

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


@app.route('/bonjour')
def bonjour():
    return 'Hello World\n'


app.run(host="0.0.0.0", port=80)
