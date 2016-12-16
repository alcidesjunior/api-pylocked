from bottle import run, request,post,get,put,delete, response,HTTPResponse, hook, Bottle
import json,md5,time
from dbase import database as db
import cryp

app = Bottle()
#
@hook('after_request')
def enable_cors():
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'PUT, GET, POST, DELETE, OPTIONS'
    response.headers['Access-Control-Allow-Headers'] = 'Origin, Accept, Content-Type, X-Requested-With, X-CSRF-Token'

@app.route('/', method = 'OPTIONS')
@app.route('/<path:path>', method = 'OPTIONS')
def options_handler(path = None):
    return

@get('/<texto>')
def c(texto):
    texto =  cryp.encode(texto)
    destex = cryp.decode(texto)
    return json.dumps({'acrip':texto,'dec':destex})
############LOGIN#############

@post('/login',method=['OPTIONS','POST'])
def logar():
    response.content_type = 'application/json'
    if request.method == 'OPTIONS':
        # print "88888888888888888888888888888888888888888888888888"
        return {}
    else:
        loginJSON = request.json

        email   =   loginJSON['email']
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
@post('/add_register',method=['OPTIONS','POST'])
def add_password():
    if request.method == 'OPTIONS':
        # print "88888888888888888888888888888888888888888888888888"
        return {}
    else:
        #get data as json
        datax        =   request.json
        #handling data as json
        system_name =   datax['system_name']
        url         =   datax['url']
        login       =   datax['login']
        password    =   cryp.encode(datax['password'])
        user_id     =   datax['user_id']

        sql = "insert into passwords values(NULL,?,?,?,?,?)"
        newpwd = db.cursor.execute(sql,(system_name,url,login,password,user_id))
        db.conn.commit()

        if newpwd:
            return json.dumps({'message':'password added successfully!','status':1})
        else:
            return json.dumps({'message':'password not added!','status':0})
@get('/list_registers/<user_id>')
def list_registers(user_id):
    sql = "select * from passwords where user_id=?"
    query = db.cursor.execute(sql,(user_id))
    all_data = db.cursor.fetchall()
    keys = ['id','system_name','url','login','password','user_id']
    i = 0
    json_data = []
    while i < len(all_data):
        json_data.append(dict(zip(keys,all_data[i])))
        i =i+1
    print "listando cadastros"
    return json.dumps(json_data)

@post('/delete_register',method=['OPTIONS','POST'])
def delete_register():
    response.content_type = 'application/json'
    if request.method == 'OPTIONS':
        print "88888888888888888888888888888888888888888888888888"
        return {}
    else:
        datax   =   request.json
        id      = datax['id']
        user_id = datax['user_id']
        query   = db.cursor.execute('DELETE FROM passwords WHERE id = ? and user_id=?', (id,user_id))
        db.conn.commit()
        if query:
            return json.dumps({"message": "Deleted with success", "status":1})
        else:
            return json.dumps({"message": "Error while delete", "status":1})

run( host='127.0.0.1', port=8080)
