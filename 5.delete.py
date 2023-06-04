import mysql.connector

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='',
)
while True:
    cursor = conexao.cursor()

    cpf = int (input('Qual é o cpf do cliente que você deseja apagar o cadastro? '))
    print (cpf)

    comando = f'DELETE FROM cliente WHERE cpf= "{cpf}"'
    cursor.execute(comando)
    conexao.commit()
    print ('LINHA EXCLUÍDA ')
    outro = int(input("Você deseja repetir? 1=SIM e 2=NÃO "))
    if (outro == 1):
        pass
    else:
        print("Informações excluidas ")
        break

cursor.close()
conexao.close()
