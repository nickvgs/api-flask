from flask import Flask, Response, request
from flask_sqlalchemy import SQLAlchemy
import mysql.connector
import json

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:admin@127.0.0.1:3306/books'
db = SQLAlchemy(app)

class books_list(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    nome_livro = db.Column(db.String(255))
    autor = db.Column(db.String(255))
    

    def to_json(self):
        return {"id":self.id, "nome_livro":self.nome_livro, "autor":self.autor}

# First Page API

@app.route("/", methods=["GET"])
def main():
    return("Hello World")


# Select for all books
@app.route("/books",methods=["GET"])
def select_books():
    select_all = books_list.query.all()
    select_all_json = [book.to_json() for book in select_all]
    
    return gera_response(200, "books", select_all_json, "ok")

# def for import response
def gera_response(status, nome_do_conteudo, conteudo, mensagem=False):
    body = {}
    body[nome_do_conteudo] = conteudo

    if(mensagem):
        body["mensagem"] = mensagem

    return Response(json.dumps(body), status=status, mimetype="application/json")

app.run()

# run to terminal for 
#   flask app.py