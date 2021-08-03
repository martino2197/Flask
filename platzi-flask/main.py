from flask import Flask, request, make_response, redirect

app = Flask(__name__)

@app.route('/')
def index():
    #vamos a regresar la ip que se obtiene del request del browser
    user_ip = request.remote_addr
    #redirecciona a /hello
    response = make_response(redirect('/hello'))
    #Ponemos una cookie que sera igual a la ip del usuario
    response.set_cookie('user_ip', user_ip)

    return response


@app.route('/hello')
def hello():
    #Obtenemos la ip del usuario desde las cookies del browser
    #vamos a regresar la ip que se obtiene del request del browser
    user_ip = request.cookies.get('user_ip')

    return 'Hello World Flask Platzi, tu IP es {}'.format(user_ip)