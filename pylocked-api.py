from bottle import auth_basic,run, post, get, put, request, response,HTTPResponse,Bottle
import json,md5,time
from dbase import database as db

app = Bottle()
@app.hook('after_request')
def enable_cors():
    print "CHAMADOsss"
	response.headers['Access-Control-Allow-Origin'] = '*'
	response.headers['Access-Control-Allow-Methods'] = 'PUT, GET, POST, DELETE, OPTIONS'
	response.headers['Access-Control-Allow-Headers'] = 'Origin, Accept, Content-Type, X-Requested-With, X-CSRF-Token'


@app.post('/login')
def logar():

	loginJSON = request.json

	email 	= 	loginJSON['email']
	pss  	= 	loginJSON['password']
	print "email"
	print email
	print pss
	sql 	= 	"select * from users where email=? and password=?"
	db.cursor.execute(sql,(email,pss))

	login = db.cursor.fetchall()

	if len(login) == 1:
		ts = time.time()
		m = md5.new(str(ts))

		token = m.hexdigest()
		return json.dumps({'auth_token': token})
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
