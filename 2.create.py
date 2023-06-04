import mysql.connector
from datetime import datetime

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='',
)
cursor = conexao.cursor()
while True:
    print ('DIGITE AS INFORMAÇÕES DO CLIENTE PARA FAZER O CADASTRO... ')

    nome = str (input('Qual o nome do cliente? '))

    cpf = int (input('Qual o CPF? '))

    data_em_texto = (input('Qual a data de nascimento ? (em formato de texto exemplo: dd/mm/YYYY )'))
    data_nasc = datetime.strptime(data_em_texto, '%d/%m/%Y').date()

    contato = int(input('Qual o número para contato? '))

    categoria_fav= str(input('Qual a categoria de livros favorita do cliente? '))

    observacoes= str(input('observações? '))

    # CREATE

    comando = f'INSERT INTO cliente (nome,cpf,data_nasc,contato,categoria_fav,observacoes) VALUES ("{nome}","{cpf}","{data_nasc}","{contato}","{categoria_fav}","{observacoes}")'
    cursor.execute(comando)
    conexao.commit()

    print("INFORMAÇÕES ADICIONADAS! ")

    outrocliente = int(input('Deseja adicionar outro cliente? 1-sim, 2- não '))

    if (outrocliente==1):
        pass
    else:
        print("INFORMAÇÕES ADICIONADAS! ")
        break

cursor.close()
conexao.close()
