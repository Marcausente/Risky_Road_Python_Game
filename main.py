import pygame, sys
from pygame.locals import *

pygame.init()

pantalla = pygame.display.set_mode((750, 750))  # Ventana de 750x750
pygame.display.set_caption("Risky Road")
logo = pygame.image.load("img/westernlogo.png")  # Carga el logo
pygame.display.set_icon(logo)

# Carga el fondo y el personaje
fondo = pygame.image.load("img/GameBackground.jpg")
pantalla.blit(fondo, (0, 0))

# Carga de imágenes del personaje
quietoarriba = pygame.image.load("img/MainCharacter/MainUpStanding.png")
caminaarriba1 = pygame.image.load("img/MainCharacter/MainUpWalking1.png")
caminaarriba2 = pygame.image.load("img/MainCharacter/MainUpWalking2.png")
quietoabajo = pygame.image.load("img\MainCharacter\MainDownStanding.png")
caminaabajo1 = pygame.image.load("img\MainCharacter\MainDownWalking1.png")
caminaabajo2 = pygame.image.load("img\MainCharacter\MainDownWalking2.png")
quietoderecha = pygame.image.load("img\MainCharacter\MainDerechaStanding.png")
caminaderecha1 = pygame.image.load("img\MainCharacter\MainDerechaWalking1.png")
caminaderecha2 = pygame.image.load("img\MainCharacter\MainDerechaWalking2.png")
quietoizquierda = pygame.image.load("img\MainCharacter\MainIzquierdaStanding.png")
caminarizquierda1 = pygame.image.load("img\MainCharacter\MainIzquierdaWalking1.png")
caminarizquierda2 = pygame.image.load("img\MainCharacter\MainIzquierdaWalking2.png")
# Redimensionamos las imágenes del personaje
quietoarriba = pygame.transform.scale(quietoarriba, (60, 60))
caminaarriba1 = pygame.transform.scale(caminaarriba1, (60, 60))
caminaarriba2 = pygame.transform.scale(caminaarriba2, (60, 60))
quietoabajo = pygame.transform.scale(quietoabajo, (60,60))
caminaabajo1 = pygame.transform.scale(caminaabajo1, (60,60))
caminaabajo2 = pygame.transform.scale(caminaabajo2, (60,60))
quietoderecha = pygame.transform.scale(quietoderecha, (60,60))
caminaderecha1 = pygame.transform.scale(caminaderecha1, (60,60))
caminaderecha2 = pygame.transform.scale(caminaderecha2, (60,60))
quietoizquierda = pygame.transform.scale(quietoizquierda, (60,60))
caminarizquierda1 = pygame.transform.scale(caminarizquierda1, (60,60))
caminarizquierda2 = pygame.transform.scale(caminarizquierda2, (60,60))
# Lista de imágenes para la animación
imagenes_caminar_arriba = [quietoarriba, caminaarriba1, quietoarriba, caminaarriba2]
imagenes_caminar_abajo = [quietoabajo, caminaabajo1, quietoabajo, caminaabajo2]
imagenes_caminar_derecha = [quietoderecha, caminaderecha1, quietoderecha, caminaderecha2]
imagenes_caminar_izquierda = [quietoizquierda, caminarizquierda1, quietoizquierda, caminarizquierda2]
indice_anim = 0  # Índice de la imagen actual en la animación
tiempo_animacion = pygame.time.get_ticks()  # Temporizador para controlar la animación

# Posición y velocidad del personaje
pos_x, pos_y = 375, 375  # Centro de la pantalla
velocidad = 0.15  # Velocidad de movimiento

# Tamaño de la pantalla y del personaje
ancho_pantalla, alto_pantalla = pantalla.get_size()
ancho_personaje, alto_personaje = quietoarriba.get_size()

while True:  # Bucle para mantener la pantalla abierta
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # Teclas presionadas
    teclas = pygame.key.get_pressed()

    # Movimiento del personaje
    if teclas[K_w]:
        pos_y -= velocidad
        # Actualizar la animación cada 200 ms
        if pygame.time.get_ticks() - tiempo_animacion > 100:
            indice_anim = (indice_anim + 1) % len(imagenes_caminar_arriba)
            tiempo_animacion = pygame.time.get_ticks()

        imagen_actual = imagenes_caminar_arriba[indice_anim]
    else:
        imagen_actual = quietoarriba  # Si no se presiona "W", mostrar la imagen quieto
    if teclas[K_s]:
        pos_y += velocidad
        if pygame.time.get_ticks() - tiempo_animacion > 100:
            indice_anim = (indice_anim + 1) % len(imagenes_caminar_abajo)
            tiempo_animacion = pygame.time.get_ticks()

        imagen_actual = imagenes_caminar_abajo[indice_anim]

    if teclas[K_a]:
        pos_x -= velocidad
        if pygame.time.get_ticks() - tiempo_animacion > 100:
            indice_anim = (indice_anim + 1) % len(imagenes_caminar_izquierda)
            tiempo_animacion = pygame.time.get_ticks()

        imagen_actual = imagenes_caminar_izquierda[indice_anim]
    if teclas[K_d]:
        pos_x += velocidad
        if pygame.time.get_ticks() - tiempo_animacion > 100:
            indice_anim = (indice_anim + 1) % len(imagenes_caminar_derecha)
            tiempo_animacion = pygame.time.get_ticks()

        imagen_actual = imagenes_caminar_derecha[indice_anim]

    # Limitar la posición dentro de los bordes de la pantalla
    pos_x = max(0, min(pos_x, ancho_pantalla - ancho_personaje))
    pos_y = max(0, min(pos_y, alto_pantalla - alto_personaje))

    # Dibujar el fondo y el personaje en la nueva posición
    pantalla.blit(fondo, (0, 0))  # Dibuja el fondo
    pantalla.blit(imagen_actual, (pos_x, pos_y))  # Dibuja la imagen actual del personaje

    pygame.display.update()  # Actualiza la pantalla
