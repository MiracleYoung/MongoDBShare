#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 5/2/18 10:31 AM
# @Author  : Miracle Young
# @File    : app.py

from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('index.html')

