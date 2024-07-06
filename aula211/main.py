# PyMySQL - um cliente MySQL feito em Python Puro
# Doc: https://pymysql.readthedocs.io/en/latest/
# Pypy: https://pypi.org/project/pymysql/
# GitHub: https://github.com/PyMySQL/PyMySQL
import pymysql
import dotenv
import os

TABLE_NAME = 'customers'
dotenv.load_dotenv()


connection = pymysql.connect(
    host=os.environ['MYSQL_HOST'],
    user=os.environ['MYSQL_USER'],
    password=os.environ['MYSQL_PASSWORD'],
    database=os.environ['MYSQL_DATABASE'],
)

# print(os.environ['MYSQL_DATABASE'])

with connection:
    with connection.cursor() as cursor:
        cursor.execute(
            f'CREATE TABLE IF NOT EXISTS {TABLE_NAME} ('
            'id INT NOT NULL AUTO_INCREMENT, '
            'nome VARCHAR(50) NOT NULL, '
            'idade INT NOT NULL, '
            'PRIMARY KEY (id)'
            ') '
        )
        # ISSO LIMPA A TABELA
        cursor.execute(f'TRUNCATE TABLE {TABLE_NAME}')
        connection.commit()

    # Começo a manipular dados a partir daqui

    # Inserindo um valor usando placeholder e um itéravel
    with connection.cursor() as cursor:
        sql =(f'INSERT INTO {TABLE_NAME} (nome, idade) VALUES (%s, %s)')
        data = ("Davi", 16)
        result = cursor.execute(sql, data)
        # print(sql)
        # print(data)
        # print(result)
    connection.commit()

    # Inserindo um valor usando placeholder e um dicionário
    with connection.cursor() as cursor:
        sql2 =(f'INSERT INTO {TABLE_NAME} (nome, idade)'
        ' VALUES (%(name)s, %(age)s) '
    )
        data2 = {
            "age": 16,
            "name": "De",
        }
            
        result2 = cursor.execute(sql2, data2)
            # print(sql2)
            # print(data2)
            # print(result2)
    connection.commit()


    # Inserindo vários valores usando placeholder e uma tupla de dicionário
    with connection.cursor() as cursor:
        sql3 =(f'INSERT INTO {TABLE_NAME} (nome, idade)'
        ' VALUES (%(name)s, %(age)s) '
    )
        data3 = (
            {"age": 18, "name": "Mauro", },
            {"age": 19, "name": "Julia", },
            {"age": 83, "name": "Ione", },
        )
            
        result2 = cursor.executemany(sql3, data3)
        # print(sql3)
        # print(data3)
        # print(result2)
    connection.commit()

        
    with connection.cursor() as cursor:
        sql2 =(f'INSERT INTO {TABLE_NAME} (nome, idade)'
        ' VALUES (%(name)s, %(age)s) '
    )
        data2 = {
            "age": 16,
            "name": "De",
        }
            
        result3 = cursor.execute(sql2, data2)
        # print(sql2)
        # print(data2)
        # print(result3)
    connection.commit()

    # Inserindo vários valores usando placeholder e uma tupla de tuplas
    with connection.cursor() as cursor:
        sql4 =(f'INSERT INTO {TABLE_NAME} (nome, idade)'
               ' VALUES (%s, %s) '
        )
        data4 = (
            ("Clau", 43),
            ("Jandrei", 29),
            )
            
        result4 = cursor.executemany(sql4, data4)
        # print(sql4)
        # print(data4)
        # print(result4)
        connection.commit()

    # Lendo os valores com SELECT
    with connection.cursor() as cursor:
        menor_id = int(input('Digite o menor id: '))
        maior_id = int(input('Digite o maior id: '))
        
        sql5 =(f'SELECT * FROM {TABLE_NAME} WHERE id BETWEEN %s AND %s ')

        cursor.execute(sql5, (menor_id, maior_id)) # type: ignore
        print(cursor.mogrify(sql5, (menor_id, maior_id))) # type: ignore
        data5 = cursor.fetchall() # type: ignore

        for row in data5:
            print(row)