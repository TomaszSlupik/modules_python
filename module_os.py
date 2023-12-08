import os

# bieżący katalog roboczy

print(os.getcwd())

print ('---')

# lista nazw plików w katalogu roboczym

print (os.listdir())

print ('---')

# lista nazw plików w katalogu roboczym które zaczynają się od litery m, posortowane
names = sorted([name for name in os.listdir() if name.startswith("m")])
print(names)

print ('---')

# posortowane alfabetycznie nazwy plików w katalogu roboczym z rozszerzeniem .py
names_py = sorted(name_py for name_py in os.listdir() if name_py.endswith(".py"))
print (names_py)

print ('---')

# stworzenie katalogu, przejście do katalogu i wyświetelnie ścieżki 
# Jeżeli istnieje to nic nie robi
if not os.path.exists('images'):
    os.mkdir('images')
    os.chdir('images')
    print (os.getcwd())
else:
    print(f"Katalog istnieje")
    
print ('---')

# stworzenie katalogu, przejście do katalogu, stworzenie katalogów dla każdego miesiąca
name_file = [] 
for i in range (1, 13):
    formatNumber = f"{i:02d}_sales"
    name_file.append(formatNumber)
    

if not os.path.exists('documents'):
    os.mkdir('documents')
    os.chdir('documents')
    for name in name_file:
        with open (name, 'w'):
            file = sorted([name for name in os.listdir()])
    print (file)
else:
    print(f"Katalog i pliki już istnieją")

print ('---')

# stworzenie katalogu, stworzenie kolejnego katalogu, wyświetlenie tych co stworzyłem 
if not os.path.exists('images'):
    os.mkdir('images')

os.chdir('images')

if not os.path.exists('images_png'):
    os.mkdir('images_png')

if not os.path.exists('images_jpg'):
    os.mkdir('images_jpg')

print("Utworzone foldery:")
for root, dirs, files in os.walk('.'):
    print(root[2:])

print ('---')

# Utworzenie katalogu Images/ przejście do katalogu Images/ utworzenie kolejnego katalogu Images
# przejście do katalogu Images i utworzenie katalogów images_jpg oraz images_png
# Utworzenie plików jpg i png o podanych skrótach w liście 

number_jpg = ['001', '004', '006', '007', '010', '016', '017', '019']
number_png = ['002', '003', '005', '008', '009', '011', '012', '013', '014', '015', '018']

if not os.path.exists('images'):
    os.mkdir('images')

os.chdir('images')

if not os.path.exists('images'):
    os.mkdir('images')

os.chdir('images')

if not os.path.exists('images_jpg'):
    os.mkdir('images_jpg')

if not os.path.exists('images_png'):
    os.mkdir('images_png')


os.chdir('images_jpg')

for name in range(len(number_jpg)):
    number_jpg[name] = number_jpg[name] + '_image.jpg'
    with open (number_jpg[name], 'w'):
        file = sorted([number_jpg for number_jpg in os.listdir()])

os.chdir('..')
os.chdir('images_png')

for name in range(len(number_png)):
    number_png[name] = number_png[name] + '_image.png'
    with open (number_png[name], 'w'):
        file = sorted([number_png for number_png in os.listdir()])

print('---')

# Wyświetlenie zawartości folderów:
content_images_png = [os.listdir()]

for name in content_images_png:
    print(name)

os.chdir('..')

os.chdir('images_jpg')

content_images_jpg = [os.listdir()]
for name in content_images_jpg:
    print(name)


print('---')

# Utworzenie folderu eval i stworzenie plików z rozszerzeniem csv

fnames = [
    '001_sales.csv',
    '002_sales.csv',
    '003_sales.csv',
    '004_sales.csv',
    '005_sales.csv',
    '006_sales.csv',
    '007_sales.csv',
    '008_sales.csv',
    '009_sales.csv',
    '010_sales.csv',
    '011_sales.csv',
    '012_sales.csv',
    '013_sales.csv',
    '014_sales.csv',
    '015_sales.csv',
    '016_sales.csv',
    '017_sales.csv',
    '018_sales.csv',
    '019_sales.csv',
    '020_sales.csv',
    '021_sales.csv',
    '022_sales.csv',
    '023_sales.csv',
    '024_sales.csv', 
]

os.chdir('../../..')

if not os.path.exists('eval'):
    os.mkdir('eval')

os.chdir('eval')


for name in fnames:
    with open (name, "w") as file:
        print (name)

print('---')

print(os.getcwd())