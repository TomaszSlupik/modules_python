import copy

# płytka kopi "copy.copy()"poniższej listy i zamiana wartości '11B' w pierwszym elemencie listy stocks na 'CRJ'.

stocks = [['CDR', '11B'], ['PLW'], ['TEN']]

stocks_copied = copy.copy(stocks)

stocks_copied[0] = ['CDR', 'CRJ']

print(f"stocks: {stocks}")
print(f"stocks_copied: {stocks_copied}")

print('---')

#  głęboką kopia poniższej listy train:

train = [['pływanie', 'pływanie'], 'rower', 'bieg']

train_copy = copy.deepcopy(train)

train_copy[0] = ['pływanie', 'rower', 'bieg']

print(train)
print(train_copy)

print('---')

# głęboka kopia - kolejny przykład - wydrukowanie kopi adresu

original_data = {
    'name': 'John',
    'age': 30,
    'address': {
        'street': '123 Main St',
        'city': 'Anytown',
        'zip': '12345'
    },
    'hobbies': ['reading', 'coding', 'swimming']
}

deep_copy_data = copy.deepcopy(original_data)

print(deep_copy_data['address'])