from ast import Delete
import sqlite3
from pathlib import Path

ROOT_DIR = Path(__file__).parent
DB_NAME = 'db.sqlite2'
DB_FILE = ROOT_DIR / DB_NAME
TABLE_NAME = 'customers'

connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()

# CRUD - Creat Reade  Update Delete
# SQL -  INSERT SELECT UPDATE DELETE


# CUIDADO: fazendo delete sem where
cursor.execute(
    f'DELETE FROM {TABLE_NAME}'
)

# DELETE mais cuidadoso 
cursor.execute(
    f'DELETE FROM sqlite_sequence WHERE name="{TABLE_NAME}"'
)

cursor.execute(
    f'DELETE FROM sqlite_sequence WHERE name="{TABLE_NAME}"'
)
connection.commit()

# Cria a tabela
cursor.execute(
    f'CREATE TABLE IF NOT EXISTS {TABLE_NAME}'
    '('
    'id INTEGER PRIMARY KEY AUTOINCREMENT,'
    'name TEXT,'
    'weight TEXT'
    ')'
)
connection.commit()

# Registrar valores nas colunas da tabela
# CUIDADO: sql injection
sql = ( 
    f'INSERT INTO {TABLE_NAME} '
    '(name, weight) '
    'VALUES '
    '(:name, :weight)'
)

# cursor.execute(sql, ['Joana', 4])
# cursor.executemany(
#     sql, 
#     (
#         ('Joana', 4), ('Luiz', 5)
#     )
# )

cursor.execute(sql, {'name': 'Davi', 'weight': 7})
cursor.executemany(sql, (
        {'name': 'Pedro', 'weight': 23},
        {'name': 'Sem nome', 'weight': 3},
        {'name': 'Com nome', 'weight': 1},
))

connection.commit()
# print(sql)

if __name__ == '__main__':
    print(sql)

    cursor.execute(
        f'DELETE FROM {TABLE_NAME} '
        'WHERE id = "4"'
    )
    connection.commit()

    cursor.execute(
        f'SELECT * FROM {TABLE_NAME}'
    )

    for row in cursor.fetchall():
        _id, name, weight = row 
        print(_id, name, weight)


    cursor.close()
    connection.close()
