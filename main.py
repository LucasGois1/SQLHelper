from SQLHelper import SQLHelper

if __name__ == '__main__':
    Alunos = SQLHelper(schema='cadastro', table='alunos')

    Alunos.insert_one({'nome': 'Lucas', 'idade': 26, 'faltas': 4}).execute()

    lista_novos_usuarios = [
        {'nome': 'Camila', 'idade': 30},
        {'nome': 'Marcio', 'idade': 35}
    ]
    Alunos.insert_many(lista_novos_usuarios).execute()

    todos_alunos_com_30_anos = Alunos.select('nome', 'faltas').where({'idade': 30}).return_all()
    print(todos_alunos_com_30_anos)

    todos_usuarios = Alunos.select().return_all()
    print(todos_usuarios)
