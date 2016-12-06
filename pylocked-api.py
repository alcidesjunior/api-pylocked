from bottle import run, post, get, put, request, response,HTTPResponse
import json, database

@post('/login')
def logar():
	response.headers['Content-Type']='application/json'

	email = request.forms.get('email')
	pss  = request.forms.get('password')
	login = cursor.execute("select count(*) as qtd from users where email='\"%s' and password='\"%s'" % (email,pss))
	if login == 1:
		retorno = json.dumps({'user': str(email) , 'password': str(pss)})
		return bottle.HTTPResponse(status=200, body=retorno)
	else:
		return bottle.HTTPResponse(status=400,body="invalid authentication")


run( host='localhost', port=3000)
