import mysql.connector

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='191102',
    database='trabalho',
)
cursor = conexao.cursor()
while True:

    a=int (input("\nVocê quer pesquisar um funcionario especifico ou ou exibir todos? Digite 1 para exibir um especifico e 2 para todos "))


    if (a==1):
        cpf = int (input('Qual é o cpf que vc quer consultar? '))
        print (cpf)
        comando = f'SELECT * FROM funcionario WHERE cpf= "{cpf}"'
        cursor.execute(comando)
        tabelafuncionario= cursor.fetchall() #exibe dados
        print ("\nEsses são os dados do funcionario de cpf", cpf,":\n", tabelafuncionario)

    elif (a==2):
        comando2 = f'SELECT * FROM funcionario'
        cursor.execute(comando2)
        tabelafuncionario= cursor.fetchall()
        print ("\nAqui está sua tabela Funcionario: ", tabelafuncionario)
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