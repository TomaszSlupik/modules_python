import urllib.request

# pobierz zawartość strony: https://www.python.org/ i wydrukuj 96 pierwszych znaków

python_url = urllib.request.urlopen('https://www.python.org/')
content = python_url.read()[:96].decode('utf-8')

print(f"{content}\n")

print('---')
# 
python_html = urllib.request.urlopen('https://www.python.org/')
content_html = python_html.read().decode('utf-8')
content_list = [line.strip() for line in content_html.splitlines() if line.strip()][:5]

for html in content_list:
    print(html)
