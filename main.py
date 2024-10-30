import pygame, sys
from pygame.locals import  *

pygame.init()

pantalla = pygame.display.set_mode((750, 750)) #Basicamente crea una ventana de 750x750
pygame.display.set_caption("Risky Road")
logo = pygame.image.load("img/westernlogo.png") #Esto carga la imagen en nuestro juego
pygame.display.set_icon(logo) #Basicamente esto carga el logo como icono del juego

#Declaramos algunos colores basicos que vamos a emplear
BLANCO = (255,255,255)
NEGRO = (0,0,0,0)
ROJO = (189, 23, 20, 1)
VERDE = (47, 197, 33, 1)
AZUL = (4, 19, 177, 1)
GREY = (76, 76, 78, 1)

pantalla.fill(GREY) #Esto pone el fondo de pantalla en gris


while True: #Este bucle se enarga de mantenter la pantalla abierta, si no se cierra solo
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update() #Actualiza el color de la pantalla al gris que hemos puesto antes