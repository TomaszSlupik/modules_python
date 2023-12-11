import re
import collections

# Liczba wystąpień poszczególnych słów: yes, no i None
target = ['yes', 'no', 'no', None, 'yes', 'yes', 'no', 'yes']

count_target = collections.Counter(target)

print(count_target)

print('---')
# Podana są wyniki głosowania w dwóch grupach głosujących w postaci słowników
# Oblicz liczbę wystąpień dla obu

poll_1 = {'yes': 140, 'no': 120, None: 12}
poll_2 = {'yes': 113, 'no': 132, None: 9}

pool_1_count = collections.Counter(poll_1)
pool_2_count = collections.Counter(poll_2)

print(pool_1_count + pool_2_count)

print('---')

#  podaj łączną liczbę głosów na 'tak' - wynik 269 głosów
pollOne = {'yes': 140, 'no': 120, None: 12}
pollTwo = {'yes': 113, 'no': 132, None: 9}
pollThree = {'yes': 16, 'no': 14}

pollOne_count = collections.Counter(pollOne)
pollTwo_count = collections.Counter(pollTwo)
pollThree_count = collections.Counter(pollThree)

all = pollOne_count + pollTwo_count + pollThree_count

print(all['yes'])

print('---')

# Liczba wystąpień liter w całym tekście
text = 'python programming - introduction'

text_count = collections.Counter(text)

print(text_count)

print('---')

# wyznacz trzy najczęściej pojawiające się znaki w podanym tekście

textPython = 'python programming - introduction'

text_Python_count = collections.Counter(textPython)

sort_text_Python_count = sorted(
    text_Python_count.items(), key=lambda x: x[1], reverse=True)

top_3 = sort_text_Python_count[:3]

print(top_3)

print('---')

# podziału podanego tekstu na wyrazy/tokeny, Dokonaj standaryzacji wyrazów (wszystkie małe litery), trzy najczęściej pojawiające się wyrazy w tekście
text = """"Python is fast enough for our site and allows us to produce maintainable features in record times,
with a minimum of developers," said Cuong Do, Software Architect, YouTube.com.

"Python plays a key role in our production pipeline. Without it a project the size of Star Wars:
Episode II would have been very difficult to pull off. From crowd rendering to batch processing to compositing,
Python binds all things together," said Tommy Burnette, Senior Technical Director, Industrial Light & Magic."""

# usuwam cudzysłowy "
text_without_quotes = re.sub(r'"', "", text)

# podział tekstu na słowa
text_split = re.compile(r'\s+')

list_textChange = re.split(text_split, text_without_quotes)

# Zamiana na małe litery
slow_list_textChange = [name.lower() for name in list_textChange]

# zliczenie
count_slow_list_textChange = collections.Counter(slow_list_textChange)

# Wybór top3
print(count_slow_list_textChange.most_common(3))

print('---')
