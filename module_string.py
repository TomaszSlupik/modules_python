
import string
import copy

# słownik a-z małe litery + wielkie litery
print(string.ascii_letters)

print('---')

# słownik a-z małe litery + przypisanie liczb od 0 do 25 
word_az = string.ascii_lowercase
my_dict = {}
range_0_25 = range(0, 26)

for name, number in zip(word_az, range_0_25):
    my_dict[name] = number

print(my_dict)

print('---')

#  string.Template i szablon e-mail wysłany do 4 osób + print 35 x '-'

names = ['John', 'Paul', 'Lisa', 'Michael']

range_x = '-'

copy_range_x = copy.copy(range_x) * 35

template_email = '''Hello ${name},
Thank you for visiting our website.
Team, XYZ'''

for name in names:
    email_template  = string.Template(template_email)
    personalized_email  = email_template.substitute(name=name)
    print(personalized_email)
    print(copy_range_x)