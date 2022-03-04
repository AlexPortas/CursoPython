import requests

import time

import csv

from bs4 import BeautifulSoup

from urllib.parse import urljoin

class PostCrawled():

    def __init__(self, titulo, emoyi, contenido, imagen):
        self.titulo = titulo
        self.emoticono = emoyi
        self.contenido = contenido
        self.imagen = imagen

class PostExtractor():

    def extraerInfo(self):
        urlBase = 'http://python.beispiel.programmierenlernen.io/index.php'
        #posts = []
        while urlBase!="":
            time.sleep(2)
            r = requests.get(urlBase)
            documento = BeautifulSoup(r.text, "html.parser")

            for card in documento.select(".card-block"):
                titulo = card.select(".card-title span")[1].text
                emoticono = card.select_one(".emoji").text
                contenido = card.select_one(".card-text").text
                imagen = urljoin(urlBase,card.select_one("img").attrs["src"])

                #crawled = PostCrawled(titulo,emoticono, contenido, imagen)
                #posts.append(crawled)

                yield PostCrawled(titulo, emoticono, contenido, imagen)
                
            btnSiguiente = documento.select_one(".navigation .btn")
            if btnSiguiente:
                rutaAbsoluta = urljoin(urlBase,documento.select_one(".navigation .btn").attrs["href"])
                print(rutaAbsoluta)
                urlBase = rutaAbsoluta
            else:
                urlBase=""


        #return posts

post = PostExtractor()
lista = post.extraerInfo()
contador=0
for p in lista:
    if contador==12:
        break
    contador+=1
    print(p.emoticono)
    print(p.titulo)
    print(p.contenido)
    print(p.imagen)
    print()

'''with open('posts.csv','w', newline='', encoding='utf-8') as csvfile:
    postwriter = csv.writer(csvfile, delimiter=';', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    for mipost in lista:
        postwriter.writerow([mipost.emoticono, mipost.titulo, mipost.contenido, mipost.imagen])'''