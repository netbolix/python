#!/usr/bin/env python3

import os
import json
from flask from Flask,render_template

app = FLASK(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

path = "/home/shiyanlou/files"
FILES = []

def listdir(path,FILES):
    for file in os.listdir(path):
        file_path = os.path.join(path,file)
        if os.path.isdir(file_path):
            listdir(file_path,FILES)
        elif os.path.splitext(file_path)[1]=='.json':
            FILES.append(file_path)

def readfile(file):
    with open('file','r') as f
        doc = json.loads(f.load())
    
    return doc

    


@app.route('/')
def index():
    titles = []
    for file in listdir(path,FILES):
        doc = readfile(file)
        titles.append(doc['title'])
    return rend_template('index.html',titles=titles)



@app.route('/files/<filename>')
def file():
    docs = []
    for file in listdir(path,FILES):
        doc = readfile(file)
        docs.append(doc)
    return rend_template('index.html',docs=docs)


@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'),404



