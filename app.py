from flask import Flask, request, make_response, jsonify
import random
app = Flask(__name__, instance_relative_config=True)

@app.route('/add')
def add():
    a = request.args.get('a', type=float)
    b = request.args.get('b', type=float)
    if a and b:
        return make_response(jsonify(s=a+b), 200) #HTTP 200 OK
    else:
        return make_response('Invalid input\n', 400) #HTTP 400 BAD REQUEST

#Endpoint /sub for subtraction which takes a and b as query parameters.
@app.route('/sub')
def sub():
    a = request.args.get('a', type=float)
    b = request.args.get('b', type=float)
    if a and b :
        return make_response(jsonify(s=a-b), 200) #HTTP 200 OK
    else:
        return make_response('Invalid input\n', 400) #HTTP 400 BAD REQUEST
#Endpoint /mul for multiplication which takes a and b as query parameters.
@app.route('/mul')
def mul():
    a = request.args.get('a', type=float)
    b = request.args.get('b', type=float)
    if a and b :
        return make_response(jsonify(s=a*b), 200) #HTTP 200 OK
    else:
        return make_response('invalid input\n', 400) #HTTP 400 BAD REQUEST
#Endpoint /div for division which takes a and b as query parameters. Returns HTTP 400 BAD REQUEST also for division by zero.
@app.route('/div')
def div():
    a = request.args.get('a', type=float)
    b = request.args.get('b', type=float)
    if a and b and b!=0:
        return make_response(jsonify(s=a/b), 200) #HTTP 200 OK
    else:
        return make_response('invalid input\n', 400) #HTTP 400 BAD REQUEST
#Endpoint /mod for modulo which takes a and b as query parameters. Returns HTTP 400 BAD REQUEST also for division by zero.
@app.route('/mod')
def mod():
    a = request.args.get('a', type=float)
    b = request.args.get('b', type=float)
    if a and b and b!=0:
        return make_response(jsonify(s=a%b), 200) #HTTP 200 OK
    else:
        return make_response('invalid input\n', 400) #HTTP 400 BAD REQUEST
#Endpoint /random which takes a and b as query parameters and returns a random number between a and b included. Returns HTTP 400 BAD REQUEST if a is greater than b.
@app.route('/random')
def random_number():
    a = request.args.get('a', type=float)
    b = request.args.get('b', type=float)
    
    # Verifica se i parametri a e b sono validi
    #questo era l'errore del 500 web servere error. cioè se a e b non sono zero.
    if a is None or b is None:
        return make_response('Invalid input\n', 400)  # HTTP 400 BAD REQUEST

    # Verifica se a è maggiore di b
    if a > b:
        return make_response('Invalid input: a should be <= b\n', 400)  # HTTP 400 BAD REQUEST

    # Restituisci un numero casuale tra a e b
    return make_response(jsonify(s=random.uniform(a, b)), 200)  # HTTP 200 OK

if __name__ == '__main__':
    app.run(debug=True)