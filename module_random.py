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
