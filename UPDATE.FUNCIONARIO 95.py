import mysql.connector
from datetime import datetime

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='191102',
    database='trabalho',
)
#UPDATE
cursor = conexao.cursor()
while True:
    alterar = int (input("Qual informação você deseja editar? Digite 1- Nome. 2-Sexo. 3-Data de nascimento. 4-Contato. 5-Email. 6-Cargo. 7-Departamento. 8-Data Admissão. 9- Salario "))
    cpf= int (input("Digite o cpf do cliente "))

    if (alterar==1):
        cursor = conexao.cursor()
        nome=str(input("Digite o novo nome: "))
        up = f' UPDATE funcionario SET Nome= "{nome}" WHERE cpf=  "{cpf}"'
        cursor.execute(up)
        conexao.commit()

    elif (alterar == 2):
        cursor = conexao.cursor()
        pergunta = str(input("Digite o sexo do funcionario: "))
        sexo = pergunta.upper()
        up = f' UPDATE funcionario SET Sexo= "{sexo}" WHERE cpf=  "{cpf}"'
        cursor.execute(up)
        conexao.commit()

    elif (alterar==3):
        cursor = conexao.cursor()
        data_em_texto = str(input("Digite o nova data de nascimento: (em formato de texto exemplo: dd/mm/YYYY)"))
        data_nasc = datetime.strptime(data_em_texto, '%d/%m/%Y').date()
        up = f' UPDATE funcionario SET Data_nasc= "{data_nasc}" WHERE cpf=  "{cpf}"'
        cursor.execute(up)
        conexao.commit()

    elif (alterar==4):
        cursor = conexao.cursor()
        contato = int(input("Digite o novo número de contato: "))
        up = f' UPDATE funcionario SET Contato= "{contato}" WHERE cpf=  "{cpf}"'
        cursor.execute(up)
        conexao.commit()

    elif (alterar==5):
        cursor = conexao.cursor()
        email = str(input("Digite o novo email: "))
        up = f' UPDATE funcionario SET Email= "{email}" WHERE cpf=  "{cpf}"'
        cursor.execute(up)
        conexao.commit()

    elif (alterar==6):
        cursor = conexao.cursor()
        cargo = str(input("Digite o novo cargo: "))
        up = f' UPDATE funcionario SET Cargo= "{cargo}" WHERE cpf=  "{cpf}"'
        cursor.execute(up)
        conexao.commit()

    elif (alterar==7):
        cursor = conexao.cursor()
        departamento = str(input("Digite o novo Departamento: "))
        up = f' UPDATE funcionario SET Departamento= "{departamento}" WHERE cpf=  "{cpf}"'
        cursor.execute(up)
        conexao.commit()

    elif (alterar == 8):
        cursor = conexao.cursor()
        data = str(input("Digite a data de admissão atualizada: (em formato de texto exemplo: dd/mm/YYYY)"))
        dataadmissao = datetime.strptime(data, '%d/%m/%Y').date()
        up = f' UPDATE funcionario SET Data_admissão= "{dataadmissao}" WHERE cpf=  "{cpf}"'
        cursor.execute(up)
        conexao.commit()

    elif (alterar == 9):
        cursor = conexao.cursor()
        salario = float(input("Digite o novo salario: "))
        up = f' UPDATE funcionario SET Salario= "{salario}" WHERE cpf=  "{cpf}"'
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