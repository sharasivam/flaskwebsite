#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 30 13:41:51 2020

@author: shara
"""

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
    
@app.route('/cakes')
def cakes():
    return render_template('cakes.html')

@app.route('/hello/<name>')
def hello(name):
    return render_template('page.html', name=name)

@app.route('/form')
def form():
    return render_template('form.html')
 
@app.route('/data', methods = ['POST', 'GET'])
def data():
    if request.method == 'GET':
        return f"The URL /data is accessed directly. Try going to '/form' to submit form"
    if request.method == 'POST':
        form_data = request.form
        return render_template('data.html',form_data = form_data)
 

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
