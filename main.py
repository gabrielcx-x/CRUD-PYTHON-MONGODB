from pymongo import MongoClient

import utilities
import crud_util

conn = MongoClient('mongodb+srv://admin:admin@mongodb-ricardo.3epehsj.mongodb.net/')
db = conn.get_database('MongoDB+Python')
colecao = db.get_collection('Produtos')
users = db.get_collection('Usuarios')

projection = {"nome": 1, "_id": 0}

user_teste = users.find({}, projection)
nomes = [user['nome'] for user in user_teste]


utilities.define_user()
nome = int(input('Opção: '))
while nome not in range(1, 4):
    print('Opção inexistente!')
    utilities.define_user()
    nome = int(input('Opção: '))
if nome == 1:
    nome_usuario = nomes[0]
if nome == 2:
    nome_usuario = nomes[1]
if nome == 3:
    nome_usuario = nomes[2]

while True:
    utilities.menu()
    resp = int(input('O que deseja fazer? Opção: '))
    while resp not in range(1, 6):
        print('Opção Inexistente!')
        utilities.menu()
        resp = int(input('O que deseja fazer? Opção: '))
    if resp == 1:
        crud_util.insert_in_collection(colecao, nome_usuario)
    if resp == 2:
        crud_util.update_in_collection(colecao)
    if resp == 3:
        crud_util.delete_in_collection(colecao)
    if resp == 4:
        crud_util.find_in_collection(colecao)
    if resp == 5:
        break

