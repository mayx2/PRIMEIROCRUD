import mysql.connector

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='',
)
cursor = conexao.cursor()
cursor.execute('CREATE TABLE livros(idlivro INT (20)AUTO_INCREMENT, codigo_do_livro BIGINT(20), titulo VARCHAR(45),numero_de_paginas INT,editora VARCHAR (20), autor VARCHAR (20),categoria VARCHAR(45),valor FLOAT,quantidade_no_estoque BIGINT(20),PRIMARY KEY (idlivro))')
