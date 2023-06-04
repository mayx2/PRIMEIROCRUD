import mysql.connector

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='',
)
cursor = conexao.cursor()
while True:

    a=int (input("\nVocê quer pesquisar uma pessoa especifica ou ou exibir todos os clientes? Digite 1 para uma pessoa e 2 para todos "))


    if (a==1):
        pergunta = int(input('DIGITE 1- PARA CONSULTAR PELO CODIGO DO LIVRO E 2- PARA CONSULTAR PELO NOME DO LIVRO '))
        if (pergunta==1):
            codigo_do_livro = int (input('Qual é o codigo do livro que você deseja consultar? '))
            comando = f'SELECT * FROM livros WHERE codigo_do_livro= "{codigo_do_livro}"'
            cursor.execute(comando)
            tabelalivro= cursor.fetchall() #exibe dados
            print ("\nEsses são os dados da livro de codigo '", codigo_do_livro,"':\n", tabelalivro)

        else:
            titulo = str(input('Qual é o nome do livro que você quer consultar? '))
            comando = f'SELECT * FROM livros WHERE titulo= "{titulo}"'
            cursor.execute(comando)
            tabelalivro = cursor.fetchall()  # exibe dados
            print("\nEsses são os dados da livro de titulo '", titulo, "':\n", tabelalivro)

    elif (a==2):
        comando2 = f'SELECT * FROM livros'
        cursor.execute(comando2)
        tabelalivro= cursor.fetchall()
        print ("\nAqui está todos os livros cadastrados: ", tabelalivro)
    else:
        print ("Codigo invalido")

    novapesquisa = int(input("\nVocê deseja fazer uma nova pesquisa? 1=Sim, 2=Não\n"))
    if (novapesquisa == 1):
         pass
    else:
     print("TUDO BEM")
     break

cursor.close()
conexao.close()


