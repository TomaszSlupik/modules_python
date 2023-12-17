import operator

# Dzielenie liczby - truediv
divide = operator.truediv(3, 5)

print(divide)

# Dzielenie całkowite - floordiv
divide_complete = operator.floordiv(5, 2)

print(divide_complete)

# wyznacz resztę z dzielenia liczby 10 przez 3 - mod
rest = operator.mod(10, 3)

print(rest)

# wyznacz liczbę 2 do potęgi 8
power = operator.pow(2, 8)

print(power)

# binarnie 
xor = operator.xor(1, 3)

print(xor)

print ('---')

# sprawdź, czy lista numbers zawiera element 4
numbers = [3, 4, 5]
myNum = 4

checkNumber = operator.contains(numbers, myNum)
print(checkNumber)

# wyciągnij element z indeksem 2 
myIndex = 2

checkIndex = operator.itemgetter(myIndex)
elementOfIndexTwo = checkIndex(numbers)
print(elementOfIndexTwo)


