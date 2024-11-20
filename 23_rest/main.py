
from flask import Flask, render_template, request, session, redirect
import os, json
import urllib.request

app = Flask(__name__)
app.secret_key = os.urandom(32)
api_key = "3aGIZiVBeJ0WXZGKSWBk5xLpAm4s60jVv3ja5FrJ"

@app.route('/')
def main():
    with urllib.request.urlopen("https://api.nasa.gov/planetary/apod?api_key=" + api_key) as response:
        html = response.read()
        str = html.decode('utf-8')
        data = json.loads(str)
        print(data)
    return render_template("html.html", explanation=data["explanation"], url=data["hdurl"])

if __name__ == "__main__": #false if this file imported as module
    app.debug = True
    app.run(port=5001)
