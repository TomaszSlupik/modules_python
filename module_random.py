import random

# ustaw ziarno losowe na wartość 42, wygeneruj pseudolosowo liczbę oraz dokładność do pięciu miejsc po przecinku.
random.seed(42)

var = random.random()

print(f"{var:.5}")

print("---")
# ustaw ziarno losowe na wartość 42, następnie wygeneruj pseudolosowo 10 liczb z przedziału [0, 1) z dokładnością do czterech miejsc po przecinku 
random.seed(42)

numbers = [random.random() for _ in range (10)]
print ([f"{num:.4}" for num in numbers])

print("---")

# ustaw ziarno losowe na wartość 42, następnie wygeneruj pseudolosowo 10 liczb z przedziału [5, 10) z dokładnością do czterech miejsc po przecinku

random.seed(42)

numbers = [random.uniform(5, 10) for _ in range(10)]

number_round = []

for num in numbers:
    number_round.append(float(f"{num: .4f}".replace(' ', '')))

print(number_round)

print("---")

import random
# ustaw ziarno losowe na wartość 42, następnie wygeneruj pseudolosowo 6 liczb całkowitych z przedziału [1, 49] (wynik losowania gry Duży Lotek) 

random.seed(42)

numbers = [random.randint(1, 49) for _ in range(6) ]

print(numbers)

print('---')

# ustaw ziarno losowe na wartość 32, następnie wylosuj jeden element z listy techs - choice

random.seed(32)

techs = ['python', 'java', 'php', 'c++', 'c#', 'javascript']

print(random.choice(techs))

print('---')

# random.choices() - wylosuj trzy elementy z listy

random.seed(32)

ran_three = [random.choices(techs) for _ in range(3) ]

unpacking_list = [item for sublist in ran_three for item in sublist]

print(unpacking_list)

print('---')

# Rozpakowanie zagnieżdżenia 
myTech = [['python'], ['typescript'], ['c#']]

unpack_myTech = [item for myItem in myTech for item in myItem]

print(unpack_myTech)

print('---')

# random.sample() 
random.seed(32)
techs = ['python', 'java', 'php', 'c++', 'c#', 'javascript']

sample_techs = random.sample(techs, k=len(techs))[:3]

print(sample_techs)

print('---')

#  dokonaj przetasowania wartości w liście techs - random.shuffle

random.seed(32)
techs = ['python', 'java', 'php', 'c++', 'c#', 'javascript']

random.shuffle(techs)

print(techs)