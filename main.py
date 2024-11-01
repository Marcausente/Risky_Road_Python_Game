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
quietoabajo = pygame.image.load("img/MainCharacter/MainDownStanding.png")
caminaabajo1 = pygame.image.load("img/MainCharacter/MainDownWalking1.png")
caminaabajo2 = pygame.image.load("img/MainCharacter/MainDownWalking2.png")
quietoderecha = pygame.image.load("img/MainCharacter/MainDerechaStanding.png")
caminaderecha1 = pygame.image.load("img/MainCharacter/MainDerechaWalking1.png")
caminaderecha2 = pygame.image.load("img/MainCharacter/MainDerechaWalking2.png")
quietoizquierda = pygame.image.load("img/MainCharacter/MainIzquierdaStanding.png")
caminarizquierda1 = pygame.image.load("img/MainCharacter/MainIzquierdaWalking1.png")
caminarizquierda2 = pygame.image.load("img/MainCharacter/MainIzquierdaWalking2.png")
arribaizquierdaquieto = pygame.image.load("img/MainCharacter/Diagonal/MainAWStanding.png")
arribaizquierda1 = pygame.image.load("img/MainCharacter/Diagonal/MainWalkingAW1.png")
arribaizquierda2 = pygame.image.load("img/MainCharacter/Diagonal/MainAWWalking2.png")
arribaderechaquieto = pygame.image.load("img/MainCharacter/Diagonal/MainWDstanding.png")
arribaderecha1 = pygame.image.load("img/MainCharacter/Diagonal/MainWalkingWD1.png")
arribaderecha2 = pygame.image.load("img/MainCharacter/Diagonal/MainWDWalking2.png")
abajoderechaquieto = pygame.image.load("img/MainCharacter/Diagonal/MainSDstanding.png")
abajoderecha1 = pygame.image.load("img/MainCharacter/Diagonal/MainWalkingSD1.png")
abajoderecha2 = pygame.image.load("img/MainCharacter/Diagonal/MainSDWalking2.png")
abajoizquierdaquieto = pygame.image.load("img/MainCharacter/Diagonal/MainSAstanding.png")
abajoizquierda1 = pygame.image.load("img/MainCharacter/Diagonal/MainWalkingSA1.png")
abajoizquierda2 = pygame.image.load("img/MainCharacter/Diagonal/MainASWalking2.png")

# Redimensionamos las imágenes del personaje
quietoarriba = pygame.transform.scale(quietoarriba, (60, 60))
caminaarriba1 = pygame.transform.scale(caminaarriba1, (60, 60))
caminaarriba2 = pygame.transform.scale(caminaarriba2, (60, 60))
quietoabajo = pygame.transform.scale(quietoabajo, (60, 60))
caminaabajo1 = pygame.transform.scale(caminaabajo1, (60, 60))
caminaabajo2 = pygame.transform.scale(caminaabajo2, (60, 60))
quietoderecha = pygame.transform.scale(quietoderecha, (60, 60))
caminaderecha1 = pygame.transform.scale(caminaderecha1, (60, 60))
caminaderecha2 = pygame.transform.scale(caminaderecha2, (60, 60))
quietoizquierda = pygame.transform.scale(quietoizquierda, (60, 60))
caminarizquierda1 = pygame.transform.scale(caminarizquierda1, (60, 60))
caminarizquierda2 = pygame.transform.scale(caminarizquierda2, (60, 60))
arribaizquierdaquieto = pygame.transform.scale(arribaizquierdaquieto, (60,60))
arribaderechaquieto = pygame.transform.scale(arribaderechaquieto, (60,60))
abajoderechaquieto = pygame.transform.scale(abajoderechaquieto,(60,60) )
abajoizquierdaquieto = pygame.transform.scale(abajoizquierdaquieto, (60,60))
abajoderecha1 = pygame.transform.scale(abajoderecha1, (60,60))
abajoderecha2 = pygame.transform.scale(abajoderecha2, (60,60))
abajoizquierda1 = pygame.transform.scale(abajoizquierda1, (60,60))
abajoizquierda2 = pygame.transform.scale(abajoizquierda2, (60,60))
arribaizquierda1 = pygame.transform.scale(arribaizquierda1, (60,60))
arribaizquierda2 = pygame.transform.scale(arribaizquierda2, (60,60))
arribaderecha2 = pygame.transform.scale(arribaderecha2, (60,60))
arribaderecha1 = pygame.transform.scale(arribaderecha1, (60,60))


# Lista de imágenes para la animación
imagenes_caminar_arriba = [quietoarriba, caminaarriba1, quietoarriba, caminaarriba2]
imagenes_caminar_abajo = [quietoabajo, caminaabajo1, quietoabajo, caminaabajo2]
imagenes_caminar_derecha = [quietoderecha, caminaderecha1, quietoderecha, caminaderecha2]
imagenes_caminar_izquierda = [quietoizquierda, caminarizquierda1, quietoizquierda, caminarizquierda2]
imagenes_arriba_izquierda = [arribaizquierdaquieto, arribaizquierda1, arribaizquierdaquieto, arribaizquierda2]
imagenes_arriba_derecha = [arribaderechaquieto, arribaderecha1, arribaderechaquieto, arribaderecha2]
imagenes_abajo_derecha = [abajoderechaquieto, abajoderecha1, abajoderechaquieto, abajoderecha2]
imagenes_abajo_izquierda = [abajoizquierdaquieto, abajoizquierda1, abajoizquierdaquieto, abajoizquierda2]
indice_anim = 0  # Índice de la imagen actual en la animación
tiempo_animacion = pygame.time.get_ticks()  # Temporizador para controlar la animación

# Posición y velocidad del personaje
pos_x, pos_y = 375, 375  # Centro de la pantalla
velocidad = 0.3  # Velocidad de movimiento
velocidad_diagonal = velocidad / 1.414  # Ajuste para movimiento diagonal

# Tamaño de la pantalla y del personaje
ancho_pantalla, alto_pantalla = pantalla.get_size()
ancho_personaje, alto_personaje = quietoarriba.get_size()

# Variable para registrar la última dirección
ultima_direccion = "abajo"  # Se inicializa con la dirección hacia abajo

while True:  # Bucle para mantener la pantalla abierta
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # Teclas presionadas
    teclas = pygame.key.get_pressed()
    movido = False  # Bandera para verificar si el personaje se ha movido

    # Movimiento diagonal y animación
    if teclas[K_w] and teclas[K_a]:  # Arriba a la izquierda
        pos_y -= velocidad_diagonal
        pos_x -= velocidad_diagonal
        ultima_direccion = "arribaizquierda"
        movido = True
        if pygame.time.get_ticks() - tiempo_animacion > 100:
            indice_anim = (indice_anim + 1) % len(imagenes_arriba_izquierda)
            tiempo_animacion = pygame.time.get_ticks()
        imagen_actual = imagenes_arriba_izquierda[indice_anim]

    elif teclas[K_w] and teclas[K_d]:  # Arriba a la derecha
        pos_y -= velocidad_diagonal
        pos_x += velocidad_diagonal
        ultima_direccion = "arribaderecha"
        movido = True
        if pygame.time.get_ticks() - tiempo_animacion > 100:
            indice_anim = (indice_anim + 1) % len(imagenes_arriba_derecha)
            tiempo_animacion = pygame.time.get_ticks()
        imagen_actual = imagenes_arriba_derecha[indice_anim]

    elif teclas[K_s] and teclas[K_a]:  # Abajo a la izquierda
        pos_y += velocidad_diagonal
        pos_x -= velocidad_diagonal
        ultima_direccion = "abajoizquierda"
        movido = True
        if pygame.time.get_ticks() - tiempo_animacion > 100:
            indice_anim = (indice_anim + 1) % len(imagenes_abajo_izquierda)
            tiempo_animacion = pygame.time.get_ticks()
        imagen_actual = imagenes_abajo_izquierda[indice_anim]

    elif teclas[K_s] and teclas[K_d]:  # Abajo a la derecha
        pos_y += velocidad_diagonal
        pos_x += velocidad_diagonal
        ultima_direccion = "abajoderecha"
        movido = True
        if pygame.time.get_ticks() - tiempo_animacion > 100:
            indice_anim = (indice_anim + 1) % len(imagenes_abajo_derecha)
            tiempo_animacion = pygame.time.get_ticks()
        imagen_actual = imagenes_abajo_derecha[indice_anim]

    # Movimiento en direcciones simples
    elif teclas[K_w]:  # Arriba
        pos_y -= velocidad
        ultima_direccion = "arriba"
        movido = True
        if pygame.time.get_ticks() - tiempo_animacion > 100:
            indice_anim = (indice_anim + 1) % len(imagenes_caminar_arriba)
            tiempo_animacion = pygame.time.get_ticks()
        imagen_actual = imagenes_caminar_arriba[indice_anim]

    elif teclas[K_s]:  # Abajo
        pos_y += velocidad
        ultima_direccion = "abajo"
        movido = True
        if pygame.time.get_ticks() - tiempo_animacion > 100:
            indice_anim = (indice_anim + 1) % len(imagenes_caminar_abajo)
            tiempo_animacion = pygame.time.get_ticks()
        imagen_actual = imagenes_caminar_abajo[indice_anim]

    elif teclas[K_a]:  # Izquierda
        pos_x -= velocidad
        ultima_direccion = "izquierda"
        movido = True
        if pygame.time.get_ticks() - tiempo_animacion > 100:
            indice_anim = (indice_anim + 1) % len(imagenes_caminar_izquierda)
            tiempo_animacion = pygame.time.get_ticks()
        imagen_actual = imagenes_caminar_izquierda[indice_anim]

    elif teclas[K_d]:  # Derecha
        pos_x += velocidad
        ultima_direccion = "derecha"
        movido = True
        if pygame.time.get_ticks() - tiempo_animacion > 100:
            indice_anim = (indice_anim + 1) % len(imagenes_caminar_derecha)
            tiempo_animacion = pygame.time.get_ticks()
        imagen_actual = imagenes_caminar_derecha[indice_anim]

    # Si no se ha movido, se muestra la imagen de quieto según la última dirección
    if not movido:
        if ultima_direccion == "arriba":
            imagen_actual = quietoarriba
        elif ultima_direccion == "abajo":
            imagen_actual = quietoabajo
        elif ultima_direccion == "izquierda":
            imagen_actual = quietoizquierda
        elif ultima_direccion == "derecha":
            imagen_actual = quietoderecha

    # Limitar la posición dentro de los bordes de la pantalla
    pos_x = max(0, min(pos_x, ancho_pantalla - ancho_personaje))
    pos_y = max(0, min(pos_y, alto_pantalla - alto_personaje))

    # Dibujar el fondo y el personaje
    pantalla.blit(fondo, (0, 0))
    pantalla.blit(imagen_actual, (pos_x, pos_y))
    pygame.display.flip()
