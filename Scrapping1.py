import requests
from bs4 import BeautifulSoup
import time

base="https://quotes.toscrape.com/page/"

with open("citas_autor.txf", "w", encoding="utf-8") as fichero:
    for pagina in range(1, 4):

        url= base+str(pagina)+"/"

        resp=requests.get(url)

        if resp.status_code==200:

            html=resp.text

            #print(html[:500])

            soup=BeautifulSoup(html, 'html.parser')
            citas=soup.find_all('div', class_='quote')
            for cita in citas:
                texto=cita.find('span', class_='text').get_text()
                autor=cita.find('small', class_='author').get_text()
                #obtener ruta del autor
                enlace=cita.find("a")["href"]
                url_autor="https://quotes.toscrape.com/"+enlace
                resp_aut=requests.get(url_autor)
                if resp_aut.status_code==200:
                    soup=BeautifulSoup(resp_aut.text, 'html.parser')
                    data_nac=soup.find('span', class_='author-born-date').get_text()
                    lugar_nac=soup.find('span', class_='author-born-location').get_text()
                    fichero.write(f"{texto} -> {autor} - {data_nac} - {lugar_nac} \n")
        else:
            print(f"Error al leer la pagina {pagina}")
        time.sleep(1)