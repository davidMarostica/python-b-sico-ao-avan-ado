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
    # PUT
    # DELETE