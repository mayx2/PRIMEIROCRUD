import mysql.connector

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='191102',
    database='trabalho',
)
cursor = conexao.cursor()
while True:

    a=int (input("\nVocê quer pesquisar uma pessoa especifica ou ou exibir todos os clientes? Digite 1 para uma pessoa e 2 para todos "))


    if (a==1):
        cpf = int (input('Qual é o cpf que vc quer consultar? '))
        print (cpf)
        comando = f'SELECT * FROM cliente WHERE cpf= "{cpf}"'
        cursor.execute(comando)
        tabelacliente= cursor.fetchall() #exibe dados
        print ("\nEsses são os dados da pessoa de cpf", cpf,":\n", tabelacliente)

    elif (a==2):
        comando2 = f'SELECT * FROM cliente'
        cursor.execute(comando2)
        tabelacliente= cursor.fetchall()
        print ("\nAqui está sua tabela Cliente: ", tabelacliente)
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


