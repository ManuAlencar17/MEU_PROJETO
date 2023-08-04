from app import app
from flask import render_template

@app.route('/')
def index():
    return render_template('index.html' , titulo = 'pagina inicial')


@app.route('/contatos')
def Contatos():
      return render_template('contatos.html' , titulo = 'contatos')

@app.route('/sobre')
def Sobre() :
     return render_template('sobre.html' , titulo = 'sobre')
     

@app.route('/projetos')
def Projetos() :
     return render_template('projetos.html' , titulo = 'Projetos')