from flask import Flask, request, jsonify, make_response, redirect, url_for, render_template, flash, get_flashed_messages
from datetime import datetime

from flask_wtf import FlaskForm

from wtforms import StringField, PasswordField, SubmitField, ValidationError
from wtforms.validators import DataRequired, Email

from flask_sqlalchemy import SQLAlchemy
import os
from dotenv import load_dotenv

# aula 1 - conexao com banco
app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///meubanco.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

# model
class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(200), unique=True, nullable=False)

# criacao de estrutura de banco
with app.app_context():
    db.create_all()

print("Banco de dados criado com sucesso!")

