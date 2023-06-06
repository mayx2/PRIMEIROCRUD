import mysql.connector

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='191102',
    database='trabalho',
)
while True:
    cursor = conexao.cursor()

    cpf = int (input('Qual é o cpf do funcionario que você deseja apagar o cadastro? '))
    print (cpf)

    comando = f'DELETE FROM funcionario WHERE cpf= "{cpf}"'
    cursor.execute(comando)
    conexao.commit()
    print ('CADASTRO EXCLUIDO! ')
    outro = int(input("Você deseja repetir? 1=SIM e 2=NÃO "))
    if (outro == 1):
        pass
    else:
        print(" CADASTRO EXCLUIDO! ")
        break

cursor.close()
conexao.close()