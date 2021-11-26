import requests

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
        r = requests.get(urlBase)
        documento = BeautifulSoup(r.text, "html.parser")
        posts = []
        for card in documento.select(".card-block"):
            titulo = card.select(".card-title span")[1].text
            emoticono = card.select_one(".emoji").text
            contenido = card.select_one(".card-text").text
            imagen = urljoin(urlBase,card.select_one("img").attrs["src"])

            crawled = PostCrawled(titulo,emoticono, contenido, imagen)
            posts.append(crawled)

        return posts

post = PostExtractor()
lista = post.extraerInfo()

for p in lista:
    print(p.emoticono)
    print(p.titulo)
    print(p.contenido)
    print(p.imagen)
    print()