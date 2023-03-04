import pygame
from pygame.locals import *
from sys import exit

pygame.init()
larg = 640
alt = 480
x = larg/2
y = 0 

tela = pygame.display.set_mode((larg,alt))
pygame.display.set_caption('PygameCurse')
relo = pygame.time.Clock()

while True: 
    relo.tick(30)
    tela.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == QUIT:
                pygame.quit()
                exit()
        pygame.draw.rect(tela,(255,0,0),(x,y,40,50))
        if y >= alt:
             y = 0
        y = y + 1;


        pygame.display.update()



