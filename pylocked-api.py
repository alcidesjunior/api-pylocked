from bottle import Bottle, run
import sqlite3

conn = sqlite3.connect('pylocked.db')
cursor = conn.cursor()

cursor.execute("""
create table users (
	id int primary key auto_increment,
	email varchar(20),
	senha varchar(64)
)
""")


app = Bottle()

@app.route('/<email>/<senha>')
def add(email, senha):
	return "seu email e %s e sua senha e %s" % (email,senha)

@app.route('/hello')
def hello():
	return "What up bro?"

run(app, host='localhost', port=3000)
