import pprint
 
# Ładniejsze wyrukowanie do konsoli - ładne formatowanie wyjścia tekstowego
data = {'name': 'John', 'age': 30, 'city': 'New York', 'hobbies': ['reading', 'traveling', 'cooking']}

pp = pprint.PrettyPrinter(indent=4)

pp.pprint(data)

# 2 przykład 
data_dict = {
    "users": [
        {
            "userId": 1,
            "firstName": "Krish",
            "lastName": "Lee",
            "emailAddress": "krish.lee@example.com"
        },
        {
            "userId": 2,
            "firstName": "racks",
            "lastName": "jacson",
            "emailAddress": "racks.jacson@example.com"
        },
        {
            "userId": 3,
            "firstName": "denial",
            "lastName": "roast",
            "emailAddress": "denial.roast@example.com"
        }
    ]
}

pp.pprint(data_dict)