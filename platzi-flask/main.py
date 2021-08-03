from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def hello():
    #vamos a regresar la ip que se obtiene del request del browser
    user_ip = request.remote_addr
    return 'Hello World Flask Platzi, tu IP es {}'.format(user_ip)