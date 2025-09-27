from flask import Flask, render_template  # corrigido: Flask, não “flase”

app = Flask(__name__)

from routes import *

if __name__ == '__main__':
    app.run(debug=True)  # roda o app em modo debug para facilitar desenvolvimento
