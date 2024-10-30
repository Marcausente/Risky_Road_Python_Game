import pygame, sys
from pygame.locals import  *

pygame.init()

pantalla = pygame.display.set_mode((800, 700)) #Basicamente crea una ventana de 500x400
pygame.display.set_caption("Risky Road")

while True: #Este bucle se enarga de mantenter la pantalla abierta, si no se cierra solo
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()