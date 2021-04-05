# -*- coding: utf-8 -*-
#"""
#Created on Sat Apr  3 21:04:11 2021

#@author: jr
#"""

from flask import Flask, Response,render_template
import pyaudio

app = Flask(__stream__)
#server = app.server

@app.route('/')
def index():
    """Video streaming home page."""
    return render_template('index.html')


if __name__ == "__main__":
    app.run()

