
import queue

# Queue - zwróci wynik 4 bo jest pierwszy w kolejce 
q = queue.Queue()

q.put(4)
q.put(1)
q.put(2)

print(q.get())

print('---')

# LifoQueue - zwróci wynik 2 bo bierze ostatni element z kolejki 
q = queue.LifoQueue()

q.put(4)
q.put(1)
q.put(2)

print(q.get())

print('---')

# Dodaje do kolejki liczby od 1 do 5 + empty () do zdejmowania elementów z kolejki 

q = queue.Queue()

for i in range (1, 6):
    q.put(i)

first_ele = q.get()
print(f"Pierwszy element z kolejki: {first_ele}")

for i in range(6, 11):
    q.put(i)

while not q.empty():
    current_ele = q.get()
    print(f"Zdejmowany element z kolejki: {current_ele}")
    pass

print ('---')
# pusta kolejkę typu LifoQueue
q = queue.LifoQueue()

for i in range (1, 4):
    q.put(i)

ele = q.get()
print (f"Element {ele}")

