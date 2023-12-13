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

# Zliczenie wystąpień zakończeń png i jpg

fnames = [
    '001_image.png',
    '002_image.png',
    '003_image.jpg',
    '004_image.png',
    '005_image.png',
    '006_image.png',
    '007_image.jpg',
    '008_image.png',
    '009_image.jpg',
    '010_image.jpg',
    '011_image.jpg',
    '012_image.png',
    '013_image.jpg',
    '014_image.jpg',
    '015_image.jpg',
    '016_image.png',
    '017_image.jpg',
    '018_image.jpg',
    '019_image.png',
    '020_image.png',
    '021_image.jpg',
    '022_image.jpg',
    '023_image.png',
    '024_image.png',
    '025_image.jpg',
    '026_image.png',
    '027_image.png',
    '028_image.jpg',
    '029_image.png',
    '030_image.png',
]

finish_fnames = []

for name in fnames:
    finish_fnames.append(name[10:])

count_finish_fnames = collections.Counter(finish_fnames)

print(count_finish_fnames)

print('---')

# Złączenie obu słowników => ChainMap

stocks_1 = {'CDR': 400, 'PLW': 490}
stocks_2 = {'PLW': 500, 'TEN': 550, 'BBT': 30}

stocks = collections.ChainMap(stocks_1, stocks_2)

print(stocks)

print('---')

# Złączenie obu słowników + Znajdź wartość dla klucza 'PLW'

stocks_3 = {'CDR': 400, 'PLW': 490}
stocks_4 = {'PLW': 500, 'TEN': 550, 'BBT': 30}

stocks_final = collections.ChainMap(stocks_3, stocks_4)

stocks_final_count = collections.Counter(stocks_final)

print(stocks_final_count['PLW'])

print('---')

#  Znajdź wartość dla klucza 'Samsung' w utworzonym obiekcie ChainMap
techs = {'Apple': 370, 'Samsung': 1100, 'Microsoft': 201}
finance = {'Citigroup': 51, 'Allianz': 180}
gaming = {'Sony': 76, 'Nintendo': 470, 'EA': 135}

sum_three = collections.ChainMap(techs, finance, gaming)

print(sum_three['Samsung'])

print('---')

# zaktualizuj wartość dla klucza 'Microsoft' w słowniku techs na 210

techs_second = {'Apple': 370, 'Samsung': 1100, 'Microsoft': 201}
finance_second = {'Citigroup': 51, 'Allianz': 180}
gaming_second = {'Sony': 76, 'Nintendo': 470, 'EA': 135}

sum_second = collections.ChainMap(techs_second, finance_second, gaming_second)

sum_second['Microsoft'] = 210

print(sum_second['Microsoft'])

print('---')

# wyświetl listę wszystkich kluczy obiektu ChainMap do konsoli posortowanych alfabetycznie.

techs_third = {'Apple': 370, 'Samsung': 1100, 'Microsoft': 201}
finance_third = {'Citigroup': 51, 'Allianz': 180}
gaming_third = {'Sony': 76, 'Nintendo': 470, 'EA': 135}

stocks_third = collections.ChainMap(techs_third, finance_third, gaming_third)

stocks_third_sort = sorted(stocks_third.keys())

print(stocks_third_sort)

print('---')

# przykład z wartościami 

class Car: 
    def __init__(self, mode='eco', power_level=7):
        self.mode = mode
        self.power_level = power_level

    def __str__(self):
        return f"{self.mode, self.power_level}"

carOne = Car()
carTwo = Car('sport', 10)

print(carTwo.mode)

print('---')

# moduł wbudowany collections oraz funkcję namedtuple(), zbuduj klasę o nazwie Point do przechowywania punktów na płaszczyźnie

Point = collections.namedtuple(typename='Point', field_names=['x', 'y'])

pointOne = Point(3, 4)
pointTwo = Point(-2, 6)

print(pointOne)
print(pointTwo)

print('---')

# Znajdź punkt będący środkiem odcinka o końcach w punktach pt1 oraz pt2

PointTwo = collections.namedtuple(typename='PointTwo', field_names=['x', 'y'])

pt1 = PointTwo(3, 4)
pt2 = PointTwo(-2, 6)

firstX = (pt1.x + pt2.x) / 2 
firstY = (pt1.y + pt2.y) / 2

final = PointTwo( firstX, firstY)
print (final)

print('---')

# podstawowe dane o utworzonych obiektach
Student = collections.namedtuple(typename='Student', field_names=['name', 'age', 'specialization'])

studentOne = Student('Mike', 21, 'physics')
studentTwo = Student('Kate', 20, 'mathematics')
studentThree = Student('Bob', 21, 'information technology')

students = [studentOne, studentTwo, studentThree]

for name in students:
    print(f"{name.name} : {name.age}: {name.specialization}")

print('---')

# Posortuj listę po wieku (atrybut age) rosnąco
People = collections.namedtuple(typename='People', field_names=['name', 'age', 'education'])

peopleOne = People('Mike', 21, 'physics')
peopleTwo = People('Mark', 22, 'biology')
peopleThree = People('Kate', 20, 'mathematics')
peopleFour = People('Bob', 21, 'information technology')

peoples = [peopleOne, peopleTwo, peopleThree, peopleFour]

peoples.sort(key=lambda x: x.age, reverse=False)

print(peoples)

print('---')
# Wydrukuj każdy jej element do konsoli.

Human = collections.namedtuple(typename='Human', field_names=['name', 'age', 'specialization'])

humanOne = {
    'name': 'Kate',
    'age': 20,
    'specialization': 'mathematics',
}

humanTwo = {
    'name': 'Mike', 
    'age': 21, 
    'specialization': 'physics'
}

humanThree = {
    'name': 'Bob',
    'age': 21,
    'specialization': 'information technology',
}

h1 = Human(humanOne['name'], humanOne['age'], humanOne['specialization'])
h2 = Human(humanTwo['name'], humanTwo['age'], humanTwo['specialization'])
h3 = Human(humanThree['name'], humanThree['age'], humanThree['specialization'])

print(h1)
print(h2)
print(h3)

print('---')