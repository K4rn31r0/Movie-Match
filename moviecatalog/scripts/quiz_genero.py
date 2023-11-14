# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 12:10:17 2023

@author: u2310421
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 12:17:51 2023

@author: PUC
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Sep 30 23:14:46 2023

@author: debor
"""

import random as r
from datetime import date

class Filme:
    def __init__(self, titulo, ano, diretor , genero, subgenero=''):
        self.genero = genero
        self.subgenero = subgenero
        self.titulo = titulo
        self.ano = ano
        self.diretor = diretor
        return
    
    def __str__ (self):
        return '{} dir. {} ({})' .format(self.titulo, self.diretor, self.ano)
    def __repr__ (self):
        return '{} dir.{} ({})' .format(self.titulo, self.diretor, self.ano)

    def getAno (self):
        return self.ano
    def getTitulo (self):
        return self.titulo
    def getGenero (self):
        return self.genero
    def getSubGenero (self):
        return self.subgenero

#database
Filme1 = Filme('Frances Ha', 2012, 'Noah Baumbach', 'Drama')
Filme2 = Filme('Little Women', 2019, 'Greta Gerwig', 'Drama')
Filme3 = Filme('Barbie', 2023, 'Greta Gerwig', 'Comédia')
Filme4 = Filme('Oppenheimer', 2023, 'Christopher Nolan', 'Drama')
Filme5 = Filme('Lady Bird', 2017, 'Greta Gerwig', 'Drama')
Filme6 = Filme('Scream VI', 2023, 'Matt Bettinelli-Olpin, Tyler Gillett', 'Terror')
Filme7 = Filme('No Hard Feelings', 2023, 'Gene Stupnitsky', 'Comédia')
Filme8 = Filme('La La Land', 2016, 'Damien Chazelle', 'Drama')
Filme9 = Filme('The Social Network', 2010, 'David Fincher', 'Drama')
Filme10 = Filme('Gone Girl', 2014, 'David Fincher', 'Suspense')
Filme11 = Filme('Knives Out', 2019, 'Rian Johnson', 'Suspense')
Filme12 = Filme('Parasite', 2019, 'Bong Joon-ho', 'Drama')
Filme13 = Filme('Pride and Prejudice', 2005, 'Joe Wright', 'Romance', 'Drama')
Filme14 = Filme('Mean Girls', 2004, 'Mark Waters', 'Comédia')
Filme15 = Filme('When Harry Met Sally...', 1989, 'Rob Reiner', 'Romance', 'Comédia')
Filme16 = Filme('Black Swan', 2010, 'Darren Aronofsky', 'Suspense')
Filme17 = Filme('The Favourite', 2018, 'Yorgos Lanthimos',  'Comédia', 'Drama')
Filme18 = Filme('Marriage Story', 2019, 'Noah Baumbach', 'Drama')
Filme19 = Filme('The Whale', 2022, 'Darren Aronofsky', 'Drama')
Filme20 = Filme('The Banshees of Inisherin', 2022, 'Martin McDonagh', 'Drama')
Filme21 = Filme('Corra!', 2017, 'Jordan Peele', 'Terror')
Filme22 = Filme('Arrival', 2016, 'Denis Villeneuve', 'Sci-Fi', 'Drama')
Filme23 = Filme('Pulp Fiction', 1995, 'Quentin Tarantino', 'Drama')
Filme24 = Filme('Infinity Pool', 2023, 'Brandon Cronenberg', 'Terror', 'Sci-Fi')
Filme25 = Filme('Asteroid City', 2023, 'Wes Anderson', 'Romance', 'Drama')

#lista database
listaFilmes = [
    Filme1, Filme2, Filme3, Filme4, Filme5,
    Filme6, Filme7, Filme8, Filme9, Filme10,
    Filme11, Filme12, Filme13, Filme14, Filme15,
    Filme16, Filme17, Filme18, Filme19, Filme20,
    Filme21, Filme22, Filme23, Filme24, Filme25
    ]

def avaliaFilme (listaFilmes):
    dicNotaUser = {}
    n = 0
    while n < 7:
        i = r.randint(0, len(listaFilmes)-1)
        filme = listaFilmes[i]
        #notaUser = int(input('Qual sua nota para o filme {}?\n Escala: \n0 - Nunca vi este filme \n1 - Muito Ruim \n2 - Ruim \n3 - Mais ou menos \n4 - Bom \n5 - Muito bom\n6 - Excelente\nNota: ' .format(filme.getTitulo())))
        notaUser = int(input('Qual sua nota para o filme {}?\n Escala: \n0 - Nunca vi este filme \n1 - Muito Ruim \n2 - Ruim \n3 - Mais ou menos \n4 - Bom \n5 - Muito bom\n6 - Excelente\nNota: ' .format(filme.title)))
        #genero = filme.getGenero()
        genero = filme.genre
        notaAtt = dicNotaUser.get(genero, None)
        if notaUser != 0:
            if notaAtt == None:
                dicNotaUser[genero] = notaUser
            else:
                dicNotaUser[genero] = (notaUser + notaAtt)/2
        listaFilmes.remove(listaFilmes[i])
        n += 1
    return dicNotaUser
        
def detGenFav (dicNotaUser):
    return max(dicNotaUser, key=dicNotaUser.get)

def detifAmigo (dicNotaUser, dicNotaUser2):
    gen_fav = detGenFav(dicNotaUser)
    gen_fav2 = detGenFav(dicNotaUser2)
    if gen_fav == gen_fav2: #its a match
        pct = detPctSemelhanca(dicNotaUser, dicNotaUser2)
        return pct
    #not a match
    return
    
def detPctSemelhanca (dicNotaUser, dicNotaUser2):
    n = 0
    l_pct = []
    while n < len(dicNotaUser):
        gen_fav = detGenFav(dicNotaUser)
        nota_genfav = dicNotaUser2.get(gen_fav, None)
        if nota_genfav != None:
            l_pct += [nota_genfav,(len(dicNotaUser)-n)]
        n += 1
    soma = 0
    peso = 0
    for lNota in enumerate(l_pct):
        soma += lNota[0] * lNota[1]
        peso += lNota[1]
    media = soma/peso
    return media


