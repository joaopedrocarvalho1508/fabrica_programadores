from main import app
from flask import render_template #usado para

@app.route('/') #a barra '/' representa a pasta raiz do site
def home():#a função está associada a rota
    return render_template('formulario.html')

@app.route('/contato')
def contato():
    return 'João, telefone 9 5050-5050'