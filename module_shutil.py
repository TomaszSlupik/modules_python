import shutil
import os
import time

# Kopiowanie zawartości z jednego dokumentu do drugiego
shutil.copy('text.txt', 'copy_text.txt')

print('---')
# Stworzenie katalogu products/ również katalogu electronics i books oraz 2 plików 
# Przeniesie pliku o nazwie product2.txt z katalogu ./products/books/ do katalogu ./products/electronics/ (shutil.move)

if not os.path.exists('products'):
    os.mkdir('products')

os.chdir('products')

print(os.getcwd())

if  not os.path.exists('electronics'):
    os.mkdir('electronics')
    os.chdir('electronics')
    with open('product1.txt', "w") as file:
        print('Plik product1.txt został uwtrozony')
    os.chdir('..')


if  not os.path.exists('books'):
    os.mkdir('books')
    os.chdir('books')
    with open ('product2.txt', "w") as file:
        print('Plik product2.txt został utworzony')
    os.chdir('..')

if os.path.exists('books/product2.txt'):
    shutil.move('books/product2.txt', 'electronics/')
else:
    print(f'Plik product2.txt nie istnieje.')

# Usuwanie katalogu
os.chdir('..')
path_data = 'data'
if not os.path.exists(path_data):
    os.mkdir(path_data)
    
if os.path.exists(path_data):
    print(f"Plik {path_data} zostanie usunięty za 5 sekund")
    time.sleep(5)
    shutil.rmtree(path_data)
    print(f"Plik {path_data} został usunięty")

# Stworzenie katalogu 'archive', archiwum (zip) z zawartością products/electronics, a następnie przeniesienie pliku zip do archive
if not os.path.exists('archive'):
    os.mkdir('archive')
    shutil.make_archive('archive', 'zip', 'products/electronics')
    shutil.move('archive.zip', 'archive')