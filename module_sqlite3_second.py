
import sqlite3

# Stworzenie bazy + dodanie 2 rekordów + wyświetlenie (bez zapisywania zmian)

connect = sqlite3.connect('my_train.db')
cursor = connect.cursor()

# tabela 
query = '''
    CREATE TABLE IF NOT EXISTS training (
        id INTEGER PRIMARY KEY,
        trening string,
        czas_min int
    )
'''

cursor.execute(query)

my_data = [
    ('rower', 90),
    ('bieg', 30)
]

cursor.executemany("INSERT INTO training (trening, czas_min) VALUES (?, ?)", my_data)

cursor.execute("select * from training")
records = cursor.fetchall()

for rec in records:
    print(rec)

