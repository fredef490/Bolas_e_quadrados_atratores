add_library('peasycam')

from bola import Bola
from retangulo import Retangulo

lista_bola = []
lista_retangulo = []

def setup():
    # fullScreen()          
    # size(1920, 1080)
    size(500, 500, P3D)
    background(100)
    rectMode(CENTER)
    cam = PeasyCam(this, 100)
    # cam.setMinimumDistance(50)
    # cam.setMaximumDistance(300)
 
def mousePressed():
    if mousePressed and (mouseButton == LEFT):       # insere novas bolas, na posicao do clique do mouse
        for i in range(int(random(2, 7))):
            nova_bola = Bola(mouseX, mouseY, 40)
            lista_bola.append(nova_bola)
    if mousePressed and (mouseButton == RIGHT):       # insere novos retangulos, na posicao do clique do mouse
        for i in range(int(random(2, 10))):
            # print("quadrado")
            novo_retangulo = Retangulo(mouseX, mouseY, random(5, 40), random(5, 20))
            lista_retangulo.append(novo_retangulo)

def keyPressed():
    if key == " ":   # limpar rastro das bolas no momento com a tecla ESPAcO
        background(100)
    if keyCode == RIGHT:    # aumentar a velocidade do movimento e consequentemente o espacamento das bolas
        for bola in lista_bola:
            bola.velocidade_pos()
        for retangulo in lista_retangulo:
            retangulo.velocidade_pos()
    if keyCode == LEFT:     # diminuir a velocidade do movimento e diminuir o espacamento das bolas
        for bola in lista_bola:
            bola.velocidade_neg()
        for retangulo in lista_retangulo:
            retangulo.velocidade_neg()

def mouseDragged():   # atração e repulcao das bolas em movimento 
    if mousePressed and (mouseButton == LEFT):
        for bola in lista_bola:
            bola.direcao()
        for retangulo in lista_retangulo:
            retangulo.direcao()
    if mousePressed and (mouseButton == RIGHT):
        for bola in lista_bola:
            bola.direcao2()
        for retangulo in lista_retangulo:
            retangulo.direcao2()

def draw():
    cursor(CROSS) #altera a forma do cursor neste caso para uma cruz
    background(100)  # caso queira que nao tenha rastros
    for bola in lista_bola:
        bola.plot()
        bola.move()
    for retangulo in lista_retangulo:
        retangulo.plot()
        retangulo.move()
