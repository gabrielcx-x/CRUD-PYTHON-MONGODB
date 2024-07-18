import utilities
from datetime import datetime

def find_in_collection(colecao):
    utilities.params_for_find()
    find_resp = int(input('O que deseja fazer? Opção: '))
    while find_resp not in range(0, 3):
        utilities.params_for_find()
        find_resp = int(input('O que deseja fazer? Opção: '))
    if find_resp == 1:
        alunos_all = list(colecao.find())
        print('Dados retornados: \n')
        for aluno in alunos_all:
            print(aluno)
        return
    id_find = input('Qual ID deseja buscar? ID: ')
    try:
        alunos = list(colecao.find({"id_produto": id_find}))
    except Exception as error:
        print('Data is not found!')
        print(error)
    else:
        print('Dados retornados: \n')
        print(alunos)

def insert_in_collection(colecao, nome_usuario):
    today = datetime.now()
    truncated_date = today.replace(hour=0, minute=0, second=0, microsecond=0)
    utilities.aviso()
    utilities.insert_dados()
    dados = {}
    dados['id_produto'] = input('ID do produto: ')
    dados['nome'] = input('Nome: ')
    dados['preco'] = float(input('Preço: '))
    dados['qnt_estoque'] = int(input('Quantidade em estoque: '))
    dados['criado_em'] = truncated_date
    dados['nome_usuario'] = nome_usuario
    try:
        colecao.insert_one(dados)
    except Exception as error:
        print('Failed to insert into the Database!')
        print(error)
    else:
        print('Added to database!')


def delete_in_collection(colecao):
    utilities.params_for_delete()
    del_resp = int(input('O que deseja fazer? Opção: '))
    while del_resp not in range(0, 3):
        utilities.params_for_delete()
        del_resp = int(input('O que deseja fazer? Opção: '))
    if del_resp == 1:
        try:
            colecao.delete_many({})
        except Exception as error:
            print('Failed to delete from database!')
            print(error)
        else:
            print('Delete succesfully!')
            return

    id_delete = input('Qual o ID do produto que deseja deletar? RA: ')
    try:
        colecao.delete_one({"id_produto": id_delete})
    except Exception as error:
        print('Failed to delete from database!')
        print(error)
    else:
        print('Deleted succesfully!')


def update_in_collection(colecao):
    utilities.params_for_update()
    up_resp = int(input('O que deseja fazer? Opção: '))
    while up_resp not in range(0, 4):
        utilities.params_for_update()
        up_resp = int(input('O que deseja fazer? Opção: '))
    id_update = input('Insira o ID do produto que será alterado: ')
    novo_dado = input('Insira o novo dado: ')
    if up_resp == 1:
        try:
            colecao.update_one({"id_produto": id_update},{"$set": {"nome": novo_dado}})
        except Exception as error:
            print('Update failed!')
            print(error)
        else:
            print('Updated succesfully!')
    if up_resp == 2:
        try:
            colecao.update_one({"id_produto": id_update},{"$set": {"preco": float(novo_dado)}})
        except Exception as error:
            print('Update failed!')
            print(error)
        else:
            print('Updated succesfully!')
    if up_resp == 3:
        try:
            colecao.update_one({"id_produto": id_update},{"$set": {"qnt_estoque": int(novo_dado)}})
        except Exception as error:
            print('Update failed!')
            print(error)
        else:
            print('Updated succesfully!')


