import mysql.connector

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='191102',
    database='trabalho',
)
while True:
    cursor = conexao.cursor()

    codigo_do_livro = int (input('Qual é o codigo do livro que você quer apagar do sistema? '))

    comando = f'DELETE FROM livros WHERE codigo_do_livro= "{codigo_do_livro}"'
    cursor.execute(comando)
    conexao.commit()
    print ('Livro excluído ')
    outro = int(input("Você deseja repetir? 1=SIM e 2=NÃO "))
    if (outro == 1):
        pass
    else:
        print("Livro excluido do sistema ")
        break

cursor.close()
conexao.close()