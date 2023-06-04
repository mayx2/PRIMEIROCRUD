import mysql.connector

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='',
)
#UPDATE
cursor = conexao.cursor()
while True:

    alterar = int (input("Qual informação você deseja editar? Digite 1- Titulo do livro. 2-numero de paginas. 3-editora. 4- Autor (a). 5-Categoria. 6-Valor. 7-Estoque"))
    codigo_do_livro= int (input("Digite o codigo do livro "))

    if (alterar==1):
        cursor = conexao.cursor()
        titulo=str(input("Digite o Titulo: "))
        up = f' UPDATE livros SET titulo= "{titulo}" WHERE codigo_do_livro=  "{codigo_do_livro}"'
        cursor.execute(up)
        conexao.commit()

    elif (alterar==2):
        cursor = conexao.cursor()
        numero_de_paginas = int (input("Digite o numero de paginas"))
        up = f' UPDATE livros SET numero_de_paginas= "{numero_de_paginas}" WHERE codigo_do_livro=  "{codigo_do_livro}"'
        cursor.execute(up)
        conexao.commit()
    elif (alterar == 3):
        cursor = conexao.cursor()
        editora = str(input("Digite o nome atualizado da editora  "))
        up = f' UPDATE livros SET editora= "{editora}" WHERE codigo_do_livro=  "{codigo_do_livro}"'
        cursor.execute(up)
        conexao.commit()

    elif (alterar==4):
        cursor = conexao.cursor()
        autor = str(input("Digite o nome do autor "))
        up = f' UPDATE livros SET autor= "{autor}" WHERE codigo_do_livro=  "{codigo_do_livro}"'
        cursor.execute(up)
        conexao.commit()

    elif (alterar==5):
        cursor = conexao.cursor()
        categoria = str(input("Digite a categoria: "))
        up = f' UPDATE livros SET categoria= "{categoria}" WHERE codigo_do_livro=  "{codigo_do_livro}"'
        cursor.execute(up)
        conexao.commit()
    elif (alterar == 6):
        cursor = conexao.cursor()
        valor = float(input("Digite o valor atualizado "))
        up = f' UPDATE livros SET valor= "{valor}" WHERE codigo_do_livro=  "{codigo_do_livro}"'
        cursor.execute(up)
        conexao.commit()

    elif (alterar==7):
        cursor = conexao.cursor()
        quantidade_no_estoque = int(input("Digite a quantidade atual do estoque "))
        up = f' UPDATE livros SET quantidade_no_estoque= "{quantidade_no_estoque}" WHERE codigo_do_livro=  "{codigo_do_livro}"'
        cursor.execute(up)
        conexao.commit()

    else:
        print("Comando invalido, tente novamente: ")

    outro = int(input("Você deseja repetir? 1=SIM e 2=NÃO "))
    if (outro==1):
        pass
    else:
        print ("INFORMAÇÕES ATUALIZADAS")
        break



cursor.close()
conexao.close()
