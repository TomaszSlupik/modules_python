import csv

# Wczytanie pliku, który jest rozdzielony przecinkiem 
apple = 'apple.csv'

with open (apple, 'r') as file:
    
    reader = csv.reader(file, delimiter=',')
    for row in reader:
        print(','.join(row))

print('---')

# Wczytanie samych kolumn 
with open (apple, 'r') as file:

    reader = csv.reader(file)    
    header = next(reader)
    header = header[0].replace(';', ',') 
    headerList = header.split(',')

print(headerList)
print('---')


# Zapis do pliku CSV - nagłówki mamy + dane 
save_my_data = 'appleTwo.csv'
headers = ['Date', 'Open', 'High', 'Low', 'Close', 'Volume']
apple = [
    [
        '1984-09-07',
        '0.4158',
        '0.4208',
        '0.4107',
        '0.4158',
        '23669718',
    ],
    [
        '1984-09-10',
        '0.4158',
        '0.4170',
        '0.4058',
        '0.4133',
        '18371562',
    ],
    [
        '1984-09-11',
        '0.4170',
        '0.4283',
        '0.4170',
        '0.4208',
        '43321235',
    ],
]

with open('apple.csv', 'w', newline='') as file:
    writer = csv.writer(file, delimiter=',')
    writer.writerow(headers)
    for row in apple:
        writer.writerow(row)