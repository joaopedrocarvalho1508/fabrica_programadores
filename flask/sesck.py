from flask import Flask #importa somente o modulo flask

app = Flask(__name__) #app é uma variavel que inicia nossa aplicação


if __name__ == '__main__':
    app.run(debug=True)

