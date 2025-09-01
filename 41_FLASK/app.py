# Aula 1 - teoria o flask

# Aula 2 - instalacao do flask
from flask import Flask, jsonify

app = Flask(__name__)


# rota login -> Site.com/login

@app.route('/')
def home():
    return "Bem-vindo ao seu primerio aplicativo Flask!"

if __name__ == '__main__':
    app.run(debug=True)