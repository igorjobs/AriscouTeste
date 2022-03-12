from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    
    nome = "Igor S"
    dados={"cargo":"CEO","empresa":"@frete.the"}
    return render_template('index.html', nome=nome,dados=dados) 

@app.route('/contato')
def contato():
    
    nome = "Igor S"
    dados={"cargo":"CEO","contatointagram":"@frete.the"}
    return render_template('contato.html', nome=nome,dados=dados)     