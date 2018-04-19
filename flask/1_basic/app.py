# -*- coding: utf-8 -*-
"""
Created on Thu Apr 19 17:14:47 2018

@author: nano

flask
"""

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/<string:page_name>/')
def render_static(page_name):
    return render_template('%s.html' % page_name)

if __name__ == '__main__':
    app.run()
    
