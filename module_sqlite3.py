import sqlite3

# utorzenie bazy danych my_database.db + połączenie 
connect = sqlite3.connect('my_database.db')
cursor = connect.cursor()

# Utworzenie tabeli 
sql_query = '''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        name TEXT,
        email TEXT
    );
'''
cursor.execute(sql_query)

# Wstawienie rekordów 
user_records = [
    ('John Doe', 'john@example.com'),
    ('Jane Smith', 'jane@example.com')
]
cursor.executemany("INSERT INTO users (name, email) VALUES (?, ?)", user_records)

# Wyświetlenie 
cursor.execute("select * from users")
records = cursor.fetchall()
for record in records:
    print(record)

# Zatwierdź zmiany 
connect.commit()

# Zamknięcie programu 
cursor.close()