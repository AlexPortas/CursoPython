import requests
from bs4 import BeautifulSoup


base="https://quotes.toscrape.com/page/"

with open("citas3.txf", "w", encoding="utf-8") as fichero:
    for pagina in range(1, 4):

        url= base+str(pagina)+"/"

        resp=requests.get(url)

        #print(resp.status_code)

        html=resp.text

        #print(html[:500])

        soup=BeautifulSoup(html, 'html.parser')
        citas=soup.find_all('div', class_='quote')
        for cita in citas:
            texto=cita.find('span', class_='text').get_text()
            autor=cita.find('small', class_='author').get_text()

            fichero.write(f"{texto} -> {autor}\n")