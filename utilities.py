import emoji


def menu():
    print("==================================")
    print("           MENU PRINCIPAL          ")
    print("==================================")
    print("1 - Inserir")
    print("2 - Alterar")
    print("3 - Deletar")
    print("4 - Consultar")
    print("5 - Sair")
    print("==================================")


def params_for_find():
    print("==================================")
    print("Deseja exibir TODOS os produtos?")
    print("1 - Sim")
    print("2 - Buscar por ID")
    print("==================================")
def insert_dados():
    print("Preencha os dados do Produto")

def aviso():
    print("⚠️AVISO! CASE-SENSITIVE!⚠️")


def params_for_delete():
    print("===========================================")
    print("Deseja deletar TODOS os produtos? (TRUNCATE)")
    print("1 - Sim")
    print("2 - Deletar produto por ID")
    print("===========================================")


def params_for_update():
    print("==================================")
    print("Deseja alterar qual DADO?")
    print("1 - Nome")
    print("2 - Preço")
    print("3 - Quantidade em estoque")
    print("==================================")


def define_user():
    print("==============================================")
    print("Defina o usuário que vai cadastrar o produto")
    print("1 - Alice")
    print("2 - Bruno")
    print("3 - Carla")
    print("==============================================")