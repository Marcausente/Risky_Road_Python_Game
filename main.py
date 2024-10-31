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


fondo = pygame.image.load("img/GameBackground.jpg")
pantalla.blit(fondo, (0, 0))
quieto = pygame.image.load("img/MainCharacter/MainUpStanding.png")
quieto = pygame.transform.scale(quieto, (60, 60)) #Redimensiona al personaje porque si no no aparece

pos_x, pos_y = 375, 375 #Esto nos coloca al personaje en el centro de la pantalla
velocidad = 0.15 #Velocidad, es baja porque es pequeño el mapa

while True: #Este bucle se enarga de mantenter la pantalla abierta, si no se cierra solo
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # Basicamente mira que tecla hay presionada
    teclas = pygame.key.get_pressed()

    # Movimiento del personaje
    if teclas[K_w]:
        pos_y -= velocidad
    if teclas[K_s]:
        pos_y += velocidad
    if teclas[K_a]:
        pos_x -= velocidad
    if teclas[K_d]:
        pos_x += velocidad

    # Dibujar el fondo y el personaje en la nueva posición
    pantalla.blit(fondo, (0, 0))  # Dibuja el fondo
    pantalla.blit(quieto, (pos_x, pos_y))  # Dibuja el personaje

    pygame.display.update()  # Actualiza la pantallawa