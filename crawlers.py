import requests

from bs4 import BeautifulSoup

r = requests.get('https://www.vontade.org/')


documento = BeautifulSoup(r.text, "html.parser")

for c in documento.find_all("body"):
    print(c)