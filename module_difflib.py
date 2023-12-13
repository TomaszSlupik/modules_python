import difflib

# porównanie dwóch ciągów znaków, podaj różnice między tekstami (różnica w słowie original/ modified)
text1 = "This is the original text."
text2 = "This is the modified text."

d = difflib.Differ()

diff = d.compare(text1.split(), text2.split())

for line in diff:
    print(line)

print('---')
# porównanie dwóch list i wyświetlenia różnic między nimi [różnica w cherry/ grape]
list1 = ["apple", "banana", "cherry", "date"]
list2 = ["apple", "banana", "grape", "date"]

list_diff = difflib.Differ()

list_diff_compare = list_diff.compare(list1, list2)

for diff in list_diff_compare:
    print(diff)