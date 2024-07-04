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

        with connection.cursor() as cursor:
            sql =(f'INSERT INTO {TABLE_NAME} (nome, idade) VALUES (%s, %s)')
            data = ("Davi", 16)
            result = cursor.execute(sql, data)
            # print(sql)
            # print(data)
            # print(result)
        connection.commit()

        with connection.cursor() as cursor:
            sql2 =(f'INSERT INTO {TABLE_NAME} (nome, idade)'
            ' VALUES (%(name)s, %(age)s) '
        )
            data2 = {
                "age": 16,
                "name": "De",
            }
            
            result2 = cursor.execute(sql2, data2)
            print(sql2)
            print(data2)
            print(result2)
        connection.commit()
