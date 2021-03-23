from fonctions import clock

from flask import Flask, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route("/")
def affichage_string():
    return clock()

if __name__=="__main__":
    app.run(debug=True)