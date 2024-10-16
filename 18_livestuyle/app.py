# heading

from flask import Flask, render_template, request, session, redirect
import os

app = Flask(__name__)

@app.route('/')
def load_page():
    return render_template("mimic.html")

if __name__ == "__main__": #false if this file imported as module
    app.debug = True
    app.run()
