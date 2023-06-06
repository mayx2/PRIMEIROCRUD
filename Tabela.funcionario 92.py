import mysql.connector

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='191102',
    database='trabalho',
)
cursor = conexao.cursor()
cursor.execute('CREATE TABLE Funcionario(idFuncionario INT (20)AUTO_INCREMENT,Nome VARCHAR(45),Sexo VARCHAR (15),Cpf BIGINT(20),Data_nasc DATETIME,Contato BIGINT(20),Email VARCHAR(50),Cargo VARCHAR(45),Departamento VARCHAR (45),Data_Admissão DATETIME,Salario float,PRIMARY KEY (idFuncionario))')

print ("Tabela criada com sucesso!")