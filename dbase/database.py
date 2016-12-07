import sqlite3

conn = sqlite3.connect('pylocked.db')
cursor = conn.cursor()

#######TABELA DE USUARIOS######
# cursor.execute("""
# create table users (
# 	id integer primary key autoincrement,
# 	email varchar(20),
# 	password varchar(64)
# )
# """)

######TABELA DE CADASTROS
