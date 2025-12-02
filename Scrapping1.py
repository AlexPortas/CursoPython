import requests
from bs4 import BeautifulSoup

url="https://quotes.toscrape.com/"

resp=requests.get(url)

#print(resp.status_code)

html=resp.text

#print(html[:500])

soup=BeautifulSoup(html, 'html.parser')
citas=soup.find_all('div', class_='quote')
print(citas[7].prettify())