# programa 1
# conecta o banco de dados; cria um cursor; insere um registro
import sqlite3
conexao = sqlite3.connect("agenda.db")
cursor = conexao.cursor()
cursor.execute('''
    create table agenda(
        nome text,
        telefone text)
    ''')
cursor.execute('''
    insert into agenda (nome, telefone)
        values(?, ?)
        ''', ("José Augusto Polizello", "99201-5114"))
conexao.commit()
cursor.close()
conexao.close()

# programa 2
# executa uma consulta no banco de dados
import sqlite3
conexao = sqlite3.connect("agenda.db")
cursor = conexao.cursor()
cursor.execute("select * from agenda")
resultado=cursor.fetchone()
print("Nome: %s\nTelefone: %s" % (resultado))
cursor.close()
conexao.close()

# programa 3
# insere múltiplos registros
import sqlite3
dados = [ ("João", "98901-0109"),
    ("André", "98902-8900"),
    ("Maria", "97891-3321")]

conexao = sqlite3.connect("agenda.db")

cursor = conexao.cursor()
cursor.executemany('''
    insert into agenda (nome, telefone)
    values(?, ?)
        ''', dados)
conexao.commit()
cursor.close()
conexao.close()

# programa 4
# consulta com múltiplos resultados

import sqlite3
conexao = sqlite3.connect("agenda.db")
cursor = conexao.cursor()
cursor.execute("select * from agenda")
resultado=cursor.fetchall()

for registro in resultado:
    print("Nome: %s\nTelefone: %s" % (registro))
    
cursor.close()
conexao.close()

# programa 5
# consulta registro por registro
import sqlite3
conexao = sqlite3.connect("agenda.db")
cursor = conexao.cursor()
cursor.execute("select * from agenda")
while True:
    resultado=cursor.fetchone()
    if resultado == None:
        break
    print("Nome: %s\nTelefone: %s" % (resultado))
cursor.close()
conexao.close()

# programa 6
# uso do with para fechar a conexão
import sqlite3
from contextlib import closing

with sqlite3.connect("agenda.db") as conexao:
    with closing(conexao.cursor()) as cursor:
        cursor.execute("select * from agenda")
        while True:
            resultado=cursor.fetchone()
            if resultado == None:
                break
            print("Nome: %s\nTelefone: %s" % (resultado))
