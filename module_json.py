import json
import pprint

# załaduj powyższy obiekt tekstowy do słownika
employees_json = """
{"IT": [{"employee_id": "0010", "stack": ["Python", "Java", "AWS", "Docker", "Linux"], "experience": 5},
{"employee_id": "0360", "stack": ["Python", "AWS", "Docker", "Linux", "Azure"], "experience": 6},
{"employee_id": "0323", "stack": ["Python", "AWS", "JavaScript"]}],
"Marketing": [{"employee_id": "0863", "stack": ["Google Analytics", "Google Ads", "Facebook Ads"]},
{"employee_id": "0543", "stack": ["Google Ads", "Facebook Ads"]}]}
"""

employees = json.loads(employees_json)
print(employees)

print('---')

# wczytanie do słownika + pprint
em_json = """
{"IT": [{"employee_id": "0010", "stack": ["Python", "Java", "AWS", "Docker", "Linux"], "experience": 5},
{"employee_id": "0360", "stack": ["Python", "AWS", "Docker", "Linux", "Azure"], "experience": 6},
{"employee_id": "0323", "stack": ["Python", "AWS", "JavaScript"]}],
"Marketing": [{"employee_id": "0863", "stack": ["Google Analytics", "Google Ads", "Facebook Ads"]},
{"employee_id": "0543", "stack": ["Google Ads", "Facebook Ads"]}]}
"""

load_em_json = json.loads(em_json)
pp_print = pprint.PrettyPrinter(indent=4)
print(pp_print.pprint(load_em_json))

print('---')

# załaduj powyższy obiekt tekstowy do słownika,
# Następnie wydrukuj do konsoli nazwy wszystkich departamentów w obiekcie

dep_json = """
{"IT": [{"employee_id": "0010", "stack": ["Python", "Java", "AWS", "Docker", "Linux"], "experience": 5},
{"employee_id": "0360", "stack": ["Python", "AWS", "Docker", "Linux", "Azure"], "experience": 6},
{"employee_id": "0323", "stack": ["Python", "AWS", "JavaScript"]}],
"Marketing": [{"employee_id": "0863", "stack": ["Google Analytics", "Google Ads", "Facebook Ads"]},
{"employee_id": "0543", "stack": ["Google Ads", "Facebook Ads"]}]}
"""

dict_dep_json = json.loads(dep_json)

for row in dict_dep_json.keys():
    print(row)

print('---')
# załaduj powyższy obiekt tekstowy do słownika
# Następnie wydrukuj do konsoli dane wszystkich pracowników działu IT

it_json = """
{"IT": [{"employee_id": "0010", "stack": ["Python", "Java", "AWS", "Docker", "Linux"], "experience": 5},
{"employee_id": "0360", "stack": ["Python", "AWS", "Docker", "Linux", "Azure"], "experience": 6},
{"employee_id": "0323", "stack": ["Python", "AWS", "JavaScript"]}],
"Marketing": [{"employee_id": "0863", "stack": ["Google Analytics", "Google Ads", "Facebook Ads"]},
{"employee_id": "0543", "stack": ["Google Ads", "Facebook Ads"]}]}
"""

data_it_json = json.loads(it_json)

data_it = []

for data in data_it_json.values():
    data_it.append(data)

for row in data_it[:1]:
    print(row[0])
    print(row[1])
    print(row[2])

print('---')

# Zapis do pliku json, a późnie odczytanie pliku
employees = {
    'IT': [
        {
            'employee_id': '0010',
            'stack': [
                'Python',
                'Java',
                'AWS',
                'Docker',
                'Linux',
            ],
            'experience': 5,
        },
        {
            'employee_id': '0360',
            'stack': [
                'Python',
                'AWS',
                'Docker',
                'Linux',
                'Azure',
            ],
            'experience': 6,
        },
        {
            'employee_id': '0323',
            'stack': [
                'Python',
                'AWS',
                'JavaScript'
            ],
        },
    ],
    'Marketing': [
        {
            'employee_id': '0863',
            'stack': [
                'Google Analytics',
                'Google Ads',
                'Facebook Ads',
            ],
        },
        {
            'employee_id': '0543',
            'stack': [
                'Google Ads',
                'Facebook Ads'
            ],
        },
    ],
}

employ_path_json = 'employees.json'

with open(employ_path_json, "w") as file:
    json.dump(employees, file, indent=4)

with open(employ_path_json, "r") as file:
    data = json.load(file)
    print(data)

print('---')

# zrzuć powyższy słownik do obiektu w formacie JSON
data_emplo = {
    'IT': [
        {
            'employee_id': '0010',
            'stack': [
                'Python',
                'Java',
                'AWS',
                'Docker',
                'Linux',
            ],
            'experience': 5,
        },
        {
            'employee_id': '0360',
            'stack': [
                'Python',
                'AWS',
                'Docker',
                'Linux',
                'Azure',
            ],
            'experience': 6,
        },
        {
            'employee_id': '0323',
            'stack': [
                'Python',
                'AWS',
                'JavaScript'
            ],
        },
    ],
    'Marketing': [
        {
            'employee_id': '0863',
            'stack': [
                'Google Analytics',
                'Google Ads',
                'Facebook Ads',
            ],
        },
        {
            'employee_id': '0543',
            'stack': [
                'Google Ads',
                'Facebook Ads'
            ],
        },
    ],
}

data_emplo_json = json.dumps(data_emplo, indent=4, sort_keys=True)

print(data_emplo_json)

print('---')


# Załaduj plik Json do słownika
print('Załadowanie pliku:')

with open('employees.json', "r") as file:
    # data = file.read()
    data = json.load(file)
    print(data)
