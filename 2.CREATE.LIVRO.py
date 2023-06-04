import mysql.connector


conexao = mysql.connector.connect(

    host='localhost',
    user='root',
    password='',
    database='',
)
cursor = conexao.cursor()
while True:

    print("CADASTRO DO LIVRO: ")
    codigo_do_livro = int (input("Digite o codigo do livro? "))
    titulo = str (input("Digite o titulo do livro? "))
    numero_de_paginas = int (input("Digite o número de paginas do livro? "))
    editora=str (input("Digite o nome da editora do livro? "))
    autor=str (input("Digite o nome do autor do livro? "))
    categoria= str (input("Digite a categoria do livro? "))
    valor = float (input("Digite o valor do livro? "))
    quantidade_no_estoque =int (input("Digite a quantidade de livros no estoque? "))


    comando = f'INSERT INTO livros (codigo_do_livro,titulo,numero_de_paginas,editora,autor,categoria,valor,quantidade_no_estoque) VALUES ("{codigo_do_livro}", "{titulo}","{numero_de_paginas}","{editora}","{autor}","{categoria}","{valor}","{quantidade_no_estoque}")'
    cursor.execute(comando)
    conexao.commit()
    outrolivro = int(input('Deseja cadastrar outro livro? 1-sim, 2- não '))
    if (outrolivro==1):
        pass
    else:
        print("LIVRO CADASTRADO! ")
        break

cursor.close()
conexao.close()
