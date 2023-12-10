
import re

# wyrażenie regularne, które szuka cyfr za pomocą findall

text = 'Python 3.10'

number = r'\d'

find_number_in_text = re.findall(number, text)

print(find_number_in_text)

print('---')

# wyrażenie regularne, które szuka liter za pomocą findall

text = 'Python 3.10'

word = r'[a-zA-Z]'

find_word_in_text = re.findall(word, text)

print(find_word_in_text)

print('---')

# wszystkie znaki nie będące zerem oraz myślnikiem 

code = '0010-000-423'

sign = r'[^0-]'

find_without = re.findall(sign, code)

print(find_without)

print('---')

# Wszytskie znaki bez znaku '-'

code = '0010-000-423-22'

codeWithout = r'[^-]'

findNumber = re.findall(codeWithout, code)
findNumberOne = ''.join(findNumber[:4])
findNumberTwo = ''.join(findNumber[4:7])
findNumberThree = ''.join(findNumber[7:10])
findNumberFour = ''.join(findNumber[10:])
finalNumber = [findNumberOne, findNumberTwo, findNumberThree, findNumberFour]

print(finalNumber)

print('---')

#  wydobądź z poniższego kodu PL i 110 i dodaj do listy

code_PL_110 = 'PL code: XG-GH-110'
re_PL_110 = r'[^code:XG-GH-]'

checkCode = re.findall(re_PL_110, code_PL_110)
checkCodePL = ''.join(checkCode[:2])
checkCode100 = ''.join(checkCode[4:])
finalCheck = [checkCodePL, checkCode100]

print(finalCheck)

print('---')

#  wszystkie tagi <>

html = """<!doctype html>

<html lang="en">
<head>
  <meta charset="utf-8">

  <title>The HTML5 Title</title>
  <meta name="description">

  <link rel="stylesheet" href="css/styles.css?v=1.0">

</head>

<body>
  <script src="js/scripts.js"></script>
</body>
</html>"""

tag = r'<([^>]+)>'

findHtml = re.findall(tag, html)

for html in findHtml:
    print (f"<{html}>")

print("---")

# z tekstu html znaleźć tag zawierający język <html lang="en">
html = """<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">

  <title>The HTML5 Title</title>
  <meta name="description">

  <link rel="stylesheet" href="css/styles.css?v=1.0">

</head>

<body>
  <script src="js/scripts.js"></script>
</body>
</html>"""

tag_html = r'<html lang="en">'

find_tag_en = re.search(tag_html, html)

print(find_tag_en.group())

print('---')

# wyciągnij z tekstu wszystkie adresy e-mail i wydrukuj do konsoli.
text = "Please send an email to info@template.com or sales-info@template.it"

firstEmail = r'info@template.com'
secondEmial = r'sales-info@template.it'

matchEmail = []
firstMatch = re.search(firstEmail, text).group()
secondMatch = re.search(secondEmial, text).group()

matchEmail.append(firstMatch)
matchEmail.append(secondMatch)

print(matchEmail)

print('---')


# odziel tekst na wyrazy/tokeny, wynik:
'''
['Python', 'plays', 'a', 'key', 'role', 'in', 'our', 'production', 'pipeline.', 'Without', 'it', 'a', 'project', 'the', 'size', 'of', 'Star', 'Wars:', 'Episode', 'II', 'would', 'have', 'been', 'very', 
'difficult', 'to', 'pull', 'off.']
'''

textTwo = """Python plays a key role in our production pipeline.
Without it a project the size of Star Wars: Episode II would have been very difficult to pull off."""

textTwo_re = re.compile(r'\s+')

textTwoNew = re.sub(textTwo_re, ',', textTwo)

word = textTwoNew.split(',')

print(word)

print('---')


# Wyszukanie wyrazów rozpoczynających się dużą literą.

textThree = """Python plays a key role in our production pipeline.
Without it a project the size of Star Wars: Episode II would have been very difficult to pull off."""

bigWord = r'\b[A-Z]\w*\b'

findBig = re.findall(bigWord, textThree)

print(findBig)

print('---')

# wyciągnij numer telefonu z podanej wiadomości
message = 'For more information, please call: 123-456-789'

message_tel = r'123-456-789'

find_tel = re.search(message_tel, message).group()

print(find_tel)

print('---')

# zamaskowanie numeru telefonu następująco '***-***-***'
text = "Please send an email to info@template.com or call to: 123-456-789."

search_number = r'\d'

change_text = re.sub(search_number, '*', text)

print(change_text)
