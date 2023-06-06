import mysql.connector
from datetime import datetime

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='191102',
    database='trabalho',
)
cursor = conexao.cursor()
while True:
    print ('DIGITE AS INFORMAÇÕES DO FUNCIONARIO PARA FAZER O CADASTRO... ')

    nome = str (input('Digite o nome do funcionario: '))
    pergunta = str(input('Digite o sexo do funcionario: '))
    sexo= pergunta.upper()
    print (sexo)
    cpf = int (input('Digite o CPF: '))

    datatexto = str(input('Digite a data de nascimento. (em formato de texto exemplo: dd/mm/YYYY )'))
    data_nasc = datetime.strptime(datatexto, '%d/%m/%Y').date()

    contato = int(input('Digite o número para contato: '))

    email= str(input('Digite o email do funcionario: '))

    cargo= str(input('Digite o cargo que o funcionario desempenha: '))
    departamento = str(input('Digite o departamento que ele pertence: '))
    datatexto2=str(input('Digite a data de admissão. (em formato de texto exemplo: dd/mm/YYYY )'))
    data_admissao = datetime.strptime(datatexto2, '%d/%m/%Y').date()
    salario=float(input('Digite o salario do funcionario: '))
    # CREATE

    comando = f'INSERT INTO funcionario (Nome,Sexo,Cpf,Data_nasc,Contato,Email,Cargo,Departamento,Data_Admissão,Salario) VALUES ("{nome}","{sexo}","{cpf}","{data_nasc}","{contato}","{email}","{cargo}","{departamento}","{data_admissao}","{salario}")'
    cursor.execute(comando)
    conexao.commit()

    print("INFORMAÇÕES ADICIONADAS! ")

    outrocliente = int(input('Deseja adicionar outro funcionario? 1-sim, 2- não '))

    if (outrocliente==1):
        pass
    else:
        print("INFORMAÇÕES ADICIONADAS! ")
        break

cursor.close()
conexao.close()