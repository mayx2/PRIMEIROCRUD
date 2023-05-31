import mysql.connector
from datetime import datetime

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='',
)
#UPDATE
cursor = conexao.cursor()
while True:
    alterar = int (input("Qual informação você deseja editar? Digite 1-nome. 2-data de nascimento. 3-contato. 4-categoria de livro favorita. 5-observações "))
    cpf= int (input("Digite o cpf do cliente "))

    if (alterar==1):
        cursor = conexao.cursor()
        nome=str(input("Digite o novo nome: "))
        cpf= "15151975498"
        up = f' UPDATE cliente SET nome= "{nome}" WHERE cpf=  "{cpf}"'
        cursor.execute(up)
        conexao.commit()

    elif (alterar==2):
        cursor = conexao.cursor()
        data_em_texto = str(input("Digite o nova data de nascimento: (em formato de texto exemplo: dd/mm/YYYY)"))
        data_nasc = datetime.strptime(data_em_texto, '%d/%m/%Y').date()
        cpf = "15151975498"
        up = f' UPDATE cliente SET data_nasc= "{data_nasc}" WHERE cpf=  "{cpf}"'
        cursor.execute(up)
        conexao.commit()

    elif (alterar==3):
        cursor = conexao.cursor()
        contato = int(input("Digite o novo número de contato: "))
        cpf = "15151975498"
        up = f' UPDATE cliente SET contato= "{contato}" WHERE cpf=  "{cpf}"'
        cursor.execute(up)
        conexao.commit()

    elif (alterar==4):
        cursor = conexao.cursor()
        categoria_fav = str(input("Digite a nova categoria de livros favorita do cliente: "))
        cpf = "15151975498"
        up = f' UPDATE cliente SET categoria_fav= "{categoria_fav}" WHERE cpf=  "{cpf}"'
        cursor.execute(up)
        conexao.commit()

    elif (alterar==5):
        cursor = conexao.cursor()
        observacoes = str(input("Digite a nova observação "))
        cpf = "15151975498"
        up = f' UPDATE cliente SET observacoes= "{observacoes}" WHERE cpf=  "{cpf}"'
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