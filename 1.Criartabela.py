import mysql.connector

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='',
)
cursor = conexao.cursor()
cursor.execute('CREATE TABLE cliente(idCliente INT (20)AUTO_INCREMENT,nome VARCHAR(45),cpf BIGINT(20),data_nasc DATETIME,contato BIGINT(20),categoria_fav VARCHAR(45),observacoes VARCHAR(45),PRIMARY KEY (idCliente))')
