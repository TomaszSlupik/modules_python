import shelve

# Dane są przechowywane pod konkretnymi kluczami, lecz dane te są przechowywane w pliku na dysku, a nie tylko w pamięci.

# Stwórz kod, który zapisuje dane do pliku o nazwie movies.db 

movies = [
    "Nietykalni",
    "Skazani na Shawshank",
    "Zielona Mila",
    "Ojciec chrzestny",
]

with shelve.open('movies') as db:
    db['movies_list'] = movies
    print('Dane zostały zapisane')


print('---')
# Odczyt pliku z bazy
with shelve.open ('movies') as db:
    movies_list = db.get('movies_list', [])
    for movies in movies_list:
        print(movies)

print('---')

# utwórz plik o nazwie my_db , a następnie zapisz trzy różne dane (imię, nazwisko i wiek) do tego pliku (klucz-wartość):
with shelve.open('my_db') as db:
    db['key'] = ['Imię', 'Nazwisko', 'Wiek']
    db['my_db'] = ['Jan', 'Kowalski', 30]


with shelve.open('my_db') as db:
    db_key = db.get('key')
    db_person = db.get('my_db')
    for key, value in zip(db_key, db_person):
        print(f"{key}: {value}")

print('---')

# Kolejny przykład - zapisanie danych treningowych do bazy 
with shelve.open('trainFriday') as db:
    db['key'] = ['id', 'trening', 'godzina', 'czas']
    db['values'] = [1, 'pływanie', '06:00', 60]
    db['valuesTwo'] = [2, 'rower', '12:00', 70]

with shelve.open('trainFriday') as db:
    key_db = db.get('key')
    value_db = db.get('values')
    value_db_two = db.get('valuesTwo')

    list_values = [value_db, value_db_two]

    print(key_db)
    print(value_db)
    print(value_db_two)
    print(f"Rozpakowana lista: {[item for list in list_values for item in list]}")