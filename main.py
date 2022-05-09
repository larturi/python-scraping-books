import bs4
import requests

class Libro():
    def __init__(self, title, stars, page):
        self.title = title
        self.stars = stars
        self.page = page


url_base = 'https://books.toscrape.com/catalogue/page-{}.html'

# Lista de libros con 4 estrellas o mas
titulos_rating_alto = []

for pagina in range(1, 4):
    url_pagina = url_base.format(pagina)
    resultado = requests.get(url_pagina)
    bs = bs4.BeautifulSoup(resultado.text, 'lxml')
    
    # Seleccionar datos de los libros
    libros = bs.select('.product_pod')
    
    # Loop Libros
    for libro in libros:
        
        # Chequear si tiene 4 o 5 estrellas
        if len(libro.select('.star-rating.Four')) > 0 or len(libro.select('.star-rating.Five')) > 0:
             
            # Guardar titulo en lista
            titulo_libro = libro.select('a')[1]['title']
            stars = 4
            if len(libro.select('.star-rating.Five')) > 0: 
                stars = 5
            libro = Libro(titulo_libro, stars, pagina)
            titulos_rating_alto.append(libro)
            

# Muestrar lista de libros
print('-'*100)
print('Libros con 5 estrellas:')
print('-'*100)
for libro in titulos_rating_alto:
    if libro.stars == 5:
        print(f'{libro.title} - Pag. {libro.page}')
        
print('-'*100)
    
print('Libros con 4 estrellas:')
print('-'*100)
for libro in titulos_rating_alto:
    if libro.stars == 4:
        print(f'{libro.title} - Pag. {libro.page}')
    