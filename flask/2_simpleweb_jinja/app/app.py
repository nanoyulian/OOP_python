# -*- coding: utf-8 -*-
"""
Created on Fri Apr 20 04:31:59 2018

@author: nano

flask-jinja2
basic

next : https://pythonspot.com/flask-and-great-looking-charts-using-chart-js/ 
"""

from flask import Flask, flash, redirect, render_template, request
from random import randint
# mengimport fungsi tambah dari file nano_libs
from nano_libs import tambah

# instansiasi objek app (flask)
app = Flask(__name__)

# http://127.0.0.0:8080/
@app.route("/")
def index():
    title = "Selamat Datang Di Halaman Home Nano"
    # fungsi untuk merender ke template *html
    return render_template('home.html',**locals())

# http://127.0.0.0:8080/user
@app.route("/user/")
def hello():
    users = ["nano","dina","nindy","icha"]
    angka = tambah(2,3)
    # **locals() mempassing variabel local ke template user.html 
    # yaitu : variabel "users" dan "angka"
    return render_template('user.html',**locals() )

# jalankan aplikasi flask dengan host 127.0.0.1, port 8080
if __name__ == "__main__":
    app.run(host='0.0.0.0',port = 8080)
    
