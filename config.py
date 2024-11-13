import math
import random

import pygame, sys
from pygame.locals import *

pygame.init()

enemigos = []
tiempo_spawn_enemigos = pygame.time.get_ticks()
tiempo_espera_inicial = 1200  # Tiempo inicial de spawn de enemigos
tiempo_espera = tiempo_espera_inicial
tiempo_spawn_enemigos = pygame.time.get_ticks()

pantalla = pygame.display.set_mode((750, 750))  # Ventana de 750x750
pygame.display.set_caption("Risky Road")
logo = pygame.image.load("img/westernlogo.png")  # Carga el logo
pygame.display.set_icon(logo)

# Carga el fondo y el personaje
fondo = pygame.image.load("img/GameBackground.jpg")

pantalla.blit(fondo, (0, 0))
# Carga de la bala
bullet = pygame.image.load("img/bullet.png")
bullet = pygame.transform.scale(bullet, (20, 20))

vidas = 3



saved = 1.0  # Variable para guardar el sonido actual, la usamos luego en controles

puntuacion = 0 #Guarda los puntos de la partida

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
diana = pygame.image.load("img/diana.png")

#FUENTE DE LETRAS
consolas = pygame.font.match_font("consolas")

#COLORES (Esto para los puntos)
ROJO = (189, 23, 20, 1)

# Redimensionamos las imágenes del personaje
fondo = pygame.transform.scale(fondo, (750, 750))
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
arribaizquierdaquieto = pygame.transform.scale(arribaizquierdaquieto, (60, 60))
arribaderechaquieto = pygame.transform.scale(arribaderechaquieto, (60, 60))
abajoderechaquieto = pygame.transform.scale(abajoderechaquieto, (60, 60))
abajoizquierdaquieto = pygame.transform.scale(abajoizquierdaquieto, (60, 60))
abajoderecha1 = pygame.transform.scale(abajoderecha1, (60, 60))
abajoderecha2 = pygame.transform.scale(abajoderecha2, (60, 60))
abajoizquierda1 = pygame.transform.scale(abajoizquierda1, (60, 60))
abajoizquierda2 = pygame.transform.scale(abajoizquierda2, (60, 60))
arribaizquierda1 = pygame.transform.scale(arribaizquierda1, (60, 60))
arribaizquierda2 = pygame.transform.scale(arribaizquierda2, (60, 60))
arribaderecha2 = pygame.transform.scale(arribaderecha2, (60, 60))
arribaderecha1 = pygame.transform.scale(arribaderecha1, (60, 60))
diana = pygame.transform.scale(diana, (60, 60))

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
velocidad = 5  # Velocidad de movimiento
velocidad_diagonal = velocidad / 1.414  # Ajuste para movimiento diagonal

# Tamaño de la pantalla y del personaje
ancho_pantalla, alto_pantalla = pantalla.get_size()
ancho_personaje, alto_personaje = quietoarriba.get_size()

# Variable para registrar la última dirección
ultima_direccion = "abajo"  # Se inicializa con la dirección hacia abajo

# Lista para almacenar los proyectiles activos
proyectiles = []
velocidad_bala = 10

tiempo_icono_visible = 10000  # Tiempo en el que el icono será visible
icono_visible = False

def reiniciar_juego():
    global puntuacion, enemigos, proyectiles, tiempo_spawn_enemigos, tiempo_espera, pos_x, pos_y
    puntuacion = 0
    enemigos = []
    proyectiles = []
    tiempo_spawn_enemigos = pygame.time.get_ticks()
    tiempo_espera = tiempo_espera_inicial
    pos_x, pos_y = ancho_pantalla // 2, alto_pantalla // 2
    pantalla.blit(fondo, (0, 0))  # Reemplazar imagen_actual con fondo

def pantalla_muerte():
    # Fondo de la pantalla de muerte
    pantalla.fill((0, 0, 0))  # Color negro de fondo
    # Mostrar mensaje de "Juego Terminado"
    muestra_texto(pantalla, consolas, "¡Juego Terminado!", ROJO, 50, ancho_pantalla // 2, alto_pantalla // 2 - 50)
    # Mostrar puntuación final
    muestra_texto(pantalla, consolas, f"Puntuación: {puntuacion}", (255, 255, 255), 30, ancho_pantalla // 2, alto_pantalla // 2)
    # Instrucción para reiniciar o salir
    muestra_texto(pantalla, consolas, "Presiona R para reiniciar o ESC para salir", (255, 255, 255), 20, ancho_pantalla // 2, alto_pantalla // 2 + 50)

    pygame.display.flip()  # Actualiza la pantalla

    # Espera hasta que el jugador presione R o ESC
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_r:  # Reiniciar el juego
                    reiniciar_juego()
                    return
                elif event.key == K_ESCAPE:  # Salir del juego
                    pygame.quit()
                    sys.exit()


def detectar_colision_bala(): #Esto es lo que detectara las colisiones de las balas
    global proyectiles, enemigos, puntuacion
    nuevos_proyectiles = []
    nuevos_enemigos = []

    for proyectil in proyectiles:
        impacto = False
        for enemigo in enemigos:
            distancia = math.hypot(proyectil["x"] - enemigo["x"], proyectil["y"] - enemigo["y"])
            if distancia < 40: #Esto es el tamaño del enemigo que generara el impacto, cuanto mas lo suba mayor sera el rango de impacto
                impacto = True
                puntuacion += 10
                break
        if not impacto:
            nuevos_proyectiles.append(proyectil)  # Mantiene las balas que no han chocado con los sprites de los enemigos
        else:
            # Solo mantiene enemigos que no han hecho contacto con las balas
            enemigos.remove(enemigo)

    for enemigo in enemigos:
        if not any(math.hypot(proyectil["x"] - enemigo["x"], proyectil["y"] - enemigo["y"]) < 20 for proyectil in
                   proyectiles):
            nuevos_enemigos.append(enemigo)

    proyectiles = nuevos_proyectiles
    enemigos = nuevos_enemigos

# Esto nos carga la musica de fondo y los sonidos
pygame.mixer.music.load("Sounds/BSO2.mp3")
shot_sound = pygame.mixer.Sound("Sounds/ShotSound.mp3")
shot_sound.set_volume(0.5)
pygame.mixer.music.play(-1)  # -1 hace que la música se reproduzca de forma infinita

# Esto es para hacer los controles de volumen, para que suba o baje según queramos
sound_up = pygame.image.load("img/Sound_UP.png")
sound_down = pygame.image.load("img/Sound_DOWN.png")
sound_on = pygame.image.load("img/Sound_ON.png")
sound_off = pygame.image.load("img/Sound_OFF.png")
sound_up = pygame.transform.scale(sound_up, (60, 60))
sound_down = pygame.transform.scale(sound_down, (60, 60))
sound_off = pygame.transform.scale(sound_off, (60, 60))
sound_on = pygame.transform.scale(sound_on, (60, 60))

# Variable para el icono de sonido actual
current_sound_icon = None

def mostrar_vidas():
    for i in range(vidas):
        vida_icono = pygame.image.load("img/LifeIcon.png")  # Cambia por la imagen de corazón o vida que tengas
        vida_icono = pygame.transform.scale(vida_icono, (30, 30))  # Ajusta el tamaño
        pantalla.blit(vida_icono, (10 + i * 40, 10))  # Coloca cada vida a la izquierda

def generar_enemigo():

    # Esto genera un enemigo random en estas posiciones: 0=arriba, 1=abajo, 2=izquierda, 3=derecha
    borde = random.randint(0, 3)
    if borde == 0:  # Borde superior
        x = random.randint(0, ancho_pantalla)
        y = 0
    elif borde == 1:  # Borde inferior
        x = random.randint(0, ancho_pantalla)
        y = alto_pantalla
    elif borde == 2:  # Borde izquierdo
        x = 0
        y = random.randint(0, alto_pantalla)
    else:  # Borde derecho
        x = ancho_pantalla
        y = random.randint(0, alto_pantalla)

    # Añadimos el enemigo a la lista de enemigos con sus coordenadas y velocidad
    enemigos.append({"x": x, "y": y, "velocidad": 3})

def mover_enemigos():
    for enemigo in enemigos:
        dx = pos_x - enemigo["x"]
        dy = pos_y - enemigo["y"]
        distancia = math.hypot(dx, dy)  # Calcula la distancia para normalizar el movimiento
        if distancia > 0:  # Evita la división por cero
            enemigo["x"] += enemigo["velocidad"] * (dx / distancia)
            enemigo["y"] += enemigo["velocidad"] * (dy / distancia)

def detectar_colision():
    for enemigo in enemigos:
        distancia = math.hypot(enemigo["x"] - pos_x, enemigo["y"] - pos_y)
        if distancia < ancho_personaje / 2:
            return True
    return False

def muestra_texto(pantalla, fuente, texto, color, dimensiones, x, y):
    tipo_letra = pygame.font.Font(consolas,dimensiones)
    superficie = tipo_letra.render(texto,False, color)
    rectangulo = superficie.get_rect()
    rectangulo.center = (x, y)
    pantalla.blit(superficie, rectangulo)