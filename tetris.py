import pygame
import random

pygame.init()

tamaño_bloque = 30 # Determina que tan grande es el bloque en píxeles
ancho_tablero = 10 # El ancho de nuestro tablero de juego en bloques
altura_tablero = 20 # Que tan alto es nuestro tablero de juego en bloques
ancho_pantalla = tamaño_bloque * (ancho_tablero + 8) # Sirve para darle espacio a los puntajes y al siguiente bloque
altura_pantalla = tamaño_bloque * altura_tablero 

# Colores para el juego

blanco =  (255,255,255)
negro = (0,0,0)
cian = (0,255,255)
azul = (0,0,225)
naranja = (255,165,0)
amarillo = (255,255,0)
verde = (0,255,0)
morado = (128,0,128)
rojo = (255,0,0)
gris = (128,128,128)

# Formas de los bloques

formas = [
    [[1,1,1,1]], # Palo
    [[1,0,0],[1,1,1]], # J
    [[0,0,1], [1,1,1]], # L
    [[1,1],[1,1]], # Cubo
    [[0,1,1],[1,1,0]], # S
    [[0,1,0],[1,1,1]], # T
    [[1,1,0],[0,1,1]] # Z
]

colores = [cian, azul, naranja, amarillo, verde, morado, rojo]

class Tetromino:
    def __init__(self):
        self.forma_idx = random.randint(a:0, len(formas) - 1)
        self.forma = [row[:] for row in formas[self.forma_idx]]
        self.color = colores[self.forma_idx]
        self.x = ancho_tablero // 2 - len(self.forma[0]) // 2
        self. y = 0

    def rotate(self):
        self.forma = [[self.forma[y][x] for y in range(len(self.forma) - 1, -1, -1)]
                      for x in range(len(self.forma[0]))]
        
class Tetris:
    def __init__(self):

