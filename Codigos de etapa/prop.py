import tkinter as tk
import random

# Configuración del juego
NUM_FILAS = 5
NUM_COLUMNAS = 5
NUM_MINAS = 3

class Buscaminas:
    def __init__(self, root):
        self.root = root
        self.root.title("Buscaminas")
        self.tablero = [[None] * NUM_COLUMNAS for _ in range(NUM_FILAS)]
        self.generar_tablero()

    def generar_tablero(self):
        for fila in range(NUM_FILAS):
            for columna in range(NUM_COLUMNAS):
                boton = tk.Button(self.root, text="", height=2, width=5, command=lambda f=fila, c=columna: self.abrir_casilla(f, c))
                boton.grid(row=fila, column=columna)
                self.tablero[fila][columna] = boton

        self.colocar_minas()







