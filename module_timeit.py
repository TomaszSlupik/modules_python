import timeit


# Wykonaj pętle code i powtórz ją 100000, oblicz czas
code = """
numbers = []
for i in range(10):
    numbers.append(i)
"""

print(timeit.timeit(code, number=100000))

print('---')

# który kod jest szybszy 
code1 = """
numbers = []
for i in range(10):
    numbers.append(i)
"""

code2 = """
numbers = [i for i in range(10)]
"""

time_code1 = timeit.timeit(code1)
time_code2 = timeit.timeit(code2)

print(time_code1)
print(time_code2)

answear_time = ['code2' if time_code1 > time_code2 else 'code1']
print(answear_time[0])


print('---')

# który kod jest szybszy dodawanie elementu na początku listy
# I - Sprawdzę dodawanie do listy za pomocą insert i za pomocą collections

first_time = """
my_list = ['java', 'javascript']
add_python = my_list.insert(0, 'python')
"""

second_time = """
import collections
second_list = ['c#', 'scala']
my_deque = collections.deque(second_list)
word_to_add = 'python'
my_deque.append(word_to_add)
second_new_list = list(my_deque)
"""

t1 = timeit.timeit(first_time)
t2 = timeit.timeit(second_time)

print(t1)
print(t2)
