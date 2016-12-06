from bottle import run, post, get, put, request, response
import json

@post('/login')
def logar():
	response.headers['Content-Type']='application/json'
	
	email = request.forms.get('email')
	pss  = request.forms.get('password')

	return json.dumps({'user': str(email) , 'password': str(pss)})

run( host='localhost', port=3000)
