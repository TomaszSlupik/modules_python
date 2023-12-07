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