import keyword

# sprawdź czy wyraz nonlocal jest słowem kluczowym w języku Python
test_nonlocal = keyword.iskeyword('nonlocal')

print(test_nonlocal)

print('---')
# wydrukuj do konsoli wszystkie słowa kluczowe dla języka Python.

word_keyword = keyword.kwlist
print(word_keyword)