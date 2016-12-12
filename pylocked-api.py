from bottle import run, request,post,get,put,delete, response,HTTPResponse#,Bottle
import json,md5,time
from dbase import database as db
import cryp

# app = Bottle()
#
# @app.hook('after_request')
# def enable_cors():
#     response.headers['Access-Control-Allow-Origin'] = '*'
#     response.headers['Access-Control-Allow-Methods'] = 'PUT, GET, POST, DELETE, OPTIONS'
#     response.headers['Access-Control-Allow-Headers'] = 'Origin, Accept, Content-Type, X-Requested-With, X-CSRF-Token'
#
# @app.route('/', method = 'OPTIONS')
# @app.route('/<path:path>', method = 'OPTIONS')
# def options_handler(path = None):
#     return

@get('/<texto>')
def c(texto):
    texto =  cryp.encode(texto)
    destex = cryp.decode(texto)
    return json.dumps({'acrip':texto,'dec':destex})
############LOGIN#############
@post('/login')
def logar():
    loginJSON = request.json

    email 	= 	loginJSON['email']
    pss  	= 	loginJSON['password']

    sql 	= 	"select * from users where email=? and password=?"
    db.cursor.execute(sql,(email,pss))

    login = db.cursor.fetchall()

    if len(login) == 1:
    	ts = time.time()
    	m = md5.new(str(ts))

    	token = m.hexdigest()
    	return json.dumps({'auth_token': token,'user_id':login[0][0]})
    else:
    	return json.dumps({'error': 'Invalid authentication'})
########FIM LOGIN######################
########ADD USUARIO####################
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
########FIM ADD USUARIO################
#######ADD PASSWORD####################
@post('/add_password')
def add_password():
    #get data as json
    data        =   request.json
    #handling data as json
    system_name =   data['system_name']
    url         =   data['url']
    email       =   data['email']
    password    =   data['password']
    user_id     =   data['user_id']

    sql = "insert into passwords values(NULL,?,?,?,?,?)"
run( host='127.0.0.1', port=8080)
