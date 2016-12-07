from bottle import run, post, get, put, request, response,HTTPResponse
import json
from dbase import database as db

@post('/login')
def logar():
	response.headers['Content-Type']='application/json'

	email = request.forms.get('email')
	pss  = request.forms.get('password')
	login = db.cursor.execute("select count(*) as qtd from users where email='\"%s' and password='\"%s'" % (email,pss))
	print login.fetchone()

	if login == 1:
		# response.status = 200
		return json.dumps({'user': str(email) , 'password': str(pss)})
	else:
		# response.status = 400
		return json.dumps({'error': 'Invalid authentication'})
@post('/add_user')
def add_user():
	response.headers['Content-Type']='application/json'
	email = request.forms.get('email')
	pss  = request.forms.get('password')
	addUser = db.cursor.execute("insert into users values(NULL, ?,?)",(email,pss))
	if addUser:
		response.status = 200
		return json.dumps({'response': 'user added'})
	else:
		response.status = 200
		response.status = 200
		return json.dumps({'response': 'not inserted'})

run( host='localhost', port=3000)
