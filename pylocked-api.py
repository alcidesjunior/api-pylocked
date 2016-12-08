from bottle import run, post, get, put, request, response,HTTPResponse
import json
from dbase import database as db

@post('/login')
def logar():
	response.headers['Content-Type']='application/json'

	email = request.forms.get('email')
	pss  = request.forms.get('password')

	sql = "select * from users where email=? and password=?"
	db.cursor.execute(sql,(email,pss))

	login = db.cursor.fetchall()

	if len(login) == 1:
		return json.dumps({'user': str(email) , 'password': str(pss)})
	else:
		return json.dumps({'error': 'Invalid authentication'})
@post('/add_user')
def add_user():
	response.headers['Content-Type']='application/json'
	email = request.forms.get('email')
	pss  = request.forms.get('password')
	addUser = db.cursor.execute("insert into users values(NULL, ?,?)",(email,pss))
	db.conn.commit()
	if addUser:
		response.status = 200
		return json.dumps({'response': 'user added'})
	else:
		response.status = 200
		response.status = 200
		return json.dumps({'response': 'not inserted'})
@get('/users')
def users():
	response.headers['Content-Type']='application/json'
	usu = db.cursor.execute("select * from users")
	usu = db.cursor.fetchall()
	return json.dumps({'result':usu})

run( host='localhost', port=3000)
