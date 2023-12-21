import zipfile

# dokonaj kompresji pliku apple.csv (najpierw odczyt pliku) a później kompresja do pliku cars.zip. 
apple = 'apple.csv'
with open (apple, "r") as file:
    content = file.read()
    print(content)

with zipfile.ZipFile ('apple.zip', 'w') as zipf:
    zipf.write(apple, compress_type=zipfile.ZIP_DEFLATED)

print('---')

# Informacje o pliku zip, jakie info i ile bajtów 
apple_zip = 'apple.zip'

info_apple_zip = zipfile.ZipInfo(apple_zip)
size_aple_zip = zipfile.ZipInfo(apple_zip).file_size

print(f"{info_apple_zip}")
print(f"{size_aple_zip} bajtów")

print('---')

# Otwórz plik tekstowy, wyświetl plik tekstowy i zapisz do zipa 
with open ('text.txt', "r", encoding='utf-8') as file:
    content = file.read()
    print(content)

with zipfile.ZipFile('text.zip', "w") as zipf:
    zipf.write('text.txt', compress_type=zipfile.ZIP_DEFLATED)


print('---')

# Rozpakuj plik zip do katalogu o nazwie backup.
import os 

if not os.path.exists('backup'):
    os.mkdir('backup')

with zipfile.ZipFile('apple.zip', "r") as zipf:
    zipf.extractall('backup')

# rawdź rozmiar pliku csv
import pathlib
with open ("appleTwo.csv", "r") as file:
    content = file.read()
    print(content)

appleTwoCsv = 'appleTwo.csv'

sizeAppleTwoCsv = pathlib.Path(appleTwoCsv).stat().st_size
kb_sizeAppleTwoCsv = round(sizeAppleTwoCsv / 1024, 1)

print(f"Rozmiar pliku top: {kb_sizeAppleTwoCsv} KB")