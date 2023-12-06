import datetime
from dateutil import parser
import locale
import calendar

# Konwert daty do yyyy-mm-dd 
firstDate = '2021-01-01'
secondDate = '31/07/21'
thirdDate = '7 maj 1990'

# Lokalizacja PL 
locale.setlocale(locale.LC_TIME, 'pl_PL.UTF-8')

print(datetime.datetime.strptime(firstDate, '%Y-%m-%d').date())
print(parser.parse(secondDate, dayfirst=True).strftime('%Y-%m-%d'))
print(datetime.datetime.strptime(thirdDate, '%d %B %Y').strftime('%Y-%m-%d'))

print('---')

# Wyświetlenie w formacie np. 12:00:00
vTime = 12

vTime_v1 = 6
vTime_v2 = 30

vTime_v3 = 9
vTime_v4 = 15

print(datetime.time(vTime))
print(datetime.time(vTime_v1, vTime_v2))
print(datetime.time(vTime_v3, vTime_v4))

print('---')
# Wyświetelnie w formacie np. 2020-07-20 11:30:00
timeOne = '2020-07-20 11:30:00'
timeTwo = '1990-03-10 12:00:00'
timeThree = '2021-01-01 00:00:00'

print (datetime.datetime.strptime(timeOne, "%Y-%m-%d %H:%M:%S"))
print(datetime.datetime.strptime(timeTwo, "%Y-%m-%d %H:%M:%S"))
print(datetime.datetime.strptime(timeThree, "%Y-%m-%d %H:%M:%S"))

print('---')

# liczba dni pomiędzy datami
a = '2020-12-31'
b = '2020-7-21'

a_date = datetime.datetime.strptime(a, '%Y-%m-%d').date()
b_date = datetime.datetime.strptime(b, '%Y-%m-%d').date()

print(f"Number of days: {(a_date - b_date).days}")

print('---')

# dokładny czas jaki upłynął pomiędzy datami

a = '2020-07-20 11:30:00'
b =  '2021-02-20 10:25:00'

a_time = datetime.datetime.strptime(a, "%Y-%m-%d %H:%M:%S")
b_time = datetime.datetime.strptime(b, "%Y-%m-%d %H:%M:%S")


print(b_time - a_time)

print('---')

# formatowanie na różne daty
'''
takie otrzymam daty w formacie:
2021-04-20
20-04-2021
04-2021
April-2021
20 April, 2021
2021-04-20 11:30:00
04/20/21 11:30:00
20(Tue) April 2021
'''
base_data = '2021-04-20 11:30:00'
locale.setlocale(locale.LC_TIME, 'en')

base_data_v1 = datetime.datetime.strptime(base_data, '%Y-%m-%d %H:%M:%S').strftime('%Y-%m-%d')
base_data_v2 = datetime.datetime.strptime(base_data, '%Y-%m-%d %H:%M:%S').strftime('%d-%m-%Y')
base_data_v3 = datetime.datetime.strptime(base_data, '%Y-%m-%d %H:%M:%S').strftime('%m-%Y')
base_data_v4 = datetime.datetime.strptime(base_data, '%Y-%m-%d %H:%M:%S')
month_base_data_v4 = calendar.month_name[base_data_v4.month]
base_data_v5 = datetime.datetime.strptime(base_data, '%Y-%m-%d %H:%M:%S')
base_data_v6 = datetime.datetime.strptime(base_data, '%Y-%m-%d %H:%M:%S').strftime('%m/%d/%Y %H:%M:%S')
base_data_v7 = datetime.datetime.strptime(base_data, '%Y-%m-%d %H:%M:%S')
month_base_data_v7 = calendar.month_name[base_data_v7.month]

print(base_data_v1)
print(base_data_v2)
print(base_data_v3)
print(f"{month_base_data_v4}-{base_data_v4.year}")
print(base_data_v5)
print(base_data_v6)
print(f"{base_data_v7.day}({base_data_v7.strftime('%a')}){month_base_data_v7} {base_data_v7.year}")

print('---')

# parsowania poniższych obiektów typu str

date_str_1 = '3 March 1995'
date_str_2 = '3/9/1995'
date_str_3 = '21-07-2021'

date_str_1_parse = datetime.datetime.strptime(date_str_1, '%d %B %Y').date().strftime('%Y-%m-%d %H:%M:%S')
print(date_str_1_parse)

date_str_2_parse = datetime.datetime.strptime(date_str_2, '%d/%m/%Y').date().strftime('%Y-%m-%d %H:%M:%S')
print(date_str_2_parse)

date_str_3_parse = datetime.datetime.strptime(date_str_3, '%d-%m-%Y').date().strftime('%Y-%m-%d %H:%M:%S')
print(date_str_3_parse)

print('---')

# liczba dni do końca obecnego roku.

now = datetime.datetime.now().strftime('%Y-%m-%d')
now_day = datetime.datetime.strptime(now, '%Y-%m-%d').date()
last_day_2023 = '2023-12-31'
last_day_2023_date = datetime.datetime.strptime(last_day_2023, '%Y-%m-%d').date()
print(f"Number of days until the end of the year: {(last_day_2023_date - now_day).days}")

print('---')

# dokładny czas pozostały do końca obecnego roku.

now = datetime.datetime.now()

end_of_year = datetime.datetime(now.year + 1, 1, 1)
diff = end_of_year - now
 
print(f'Until the end of the year: {diff}')


print('---')

# dodawanie do daty (dni, godzin lub min)
'''
z daty 2020-01-01 00:00:00 otrzymam datę:
-przesuniętą o 7 dni
-przesuniętą o 30 dni
-przesuniętą o 30 godzin
-przesuniętą o 15 minut
'''

test_data = '2020-01-01 00:00:00'

test_data_add_7_days = datetime.datetime.strptime(test_data, '%Y-%m-%d %H:%M:%S') + datetime.timedelta(days=7)
test_data_add_30_days = datetime.datetime.strptime(test_data, '%Y-%m-%d %H:%M:%S') + datetime.timedelta(days=30)
test_data_add_30_h = datetime.datetime.strptime(test_data, '%Y-%m-%d %H:%M:%S') + datetime.timedelta(hours=30)
test_data_add_15_min = datetime.datetime.strptime(test_data, '%Y-%m-%d %H:%M:%S') + datetime.timedelta(minutes=15)

print(test_data_add_7_days)
print(test_data_add_30_days)
print(test_data_add_30_h)
print(test_data_add_15_min)

print('---')

# Wydrukowanie pełnych dat i godzin z całej listy

dates = [
    datetime.datetime(2020, 1, 1, 0, 0),
    datetime.datetime(2020, 1, 1, 8, 0),
    datetime.datetime(2020, 1, 1, 16, 0),
    datetime.datetime(2020, 1, 2, 0, 0),
    datetime.datetime(2020, 1, 2, 8, 0),
    datetime.datetime(2020, 1, 2, 16, 0),
    datetime.datetime(2020, 1, 3, 0, 0),
    datetime.datetime(2020, 1, 3, 8, 0),
    datetime.datetime(2020, 1, 3, 16, 0),
    datetime.datetime(2020, 1, 4, 0, 0),
    datetime.datetime(2020, 1, 4, 8, 0),
    datetime.datetime(2020, 1, 4, 16, 0),
]

for date in dates:
    print(date.strftime('%Y-%m-%d %H:%M:%S'))