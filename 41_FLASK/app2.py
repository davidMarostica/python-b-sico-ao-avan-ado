# aula 1- continuando rotas
from flask import Flask, request, jsonify, make_response, redirect, url_for, render_template
from datetime import datetime

app = Flask(__name__)

@app.route("/api", methods=["GET", "POST", "PUT", "DELETE"])
def api():
    if request.method == "GET":
        return jsonify({"message": "Método GET ativado."})
    elif request.method == "POST":
        return jsonify({"message": "Método POST ativado."})
    elif request.method == "PUT":
        return jsonify({"message": "Método PUT ativado."})
    elif request.method == "DELETE":
        return jsonify({"message": "Método DELETE ativado."})

@app.route("/")
def home():
    return "Bem-vindo ao seu primeiro app de Flask!"

if __name__ == "__main__":
    app.run(debug=True)