# -*- coding: utf-8 -*-
"""
Created on Thu Apr 19 17:06:58 2018

@author: nano

latihan flask
"""

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hallo Nano Web App with Flask"
    
if __name__ == "__main__":
    app.run()
