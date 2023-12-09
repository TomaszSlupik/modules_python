import sys 

# ścieżka dla pliku binarnego
print(sys.executable)

print("---")

# Lista Modułów
print(sys.path)

print("---")

# przekazane argumenty
for arg in sys.argv[1:]:
    print (arg)

print("---")

