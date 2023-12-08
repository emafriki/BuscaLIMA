import tkinter as tk
import random

#anadir boton para preguntar que nivel desea jugar


# Configuración del juego
NUM_FILAS = 5
NUM_COLUMNAS = 5
NUM_MINAS = 3

class Buscaminas:                            #Representa el juego
    def __init__(self, root):
        self.root = root
        self.root.title("Buscaminas")
        self.tablero = [[None] * NUM_COLUMNAS for _ in range(NUM_FILAS)]
        self.generar_tablero()

    def generar_tablero(self):               # creamos una cuadrícula de botones utilizando `Button` de `tkinter` 
        for fila in range(NUM_FILAS):        # y los almacenamos en la matriz `tablero`.
            for columna in range(NUM_COLUMNAS):
                boton = tk.Button(self.root, text="", height=2, width=5, command=lambda f=fila, c=columna: self.abrir_casilla(f, c))
                boton.grid(row=fila, column=columna)
                self.tablero[fila][columna] = boton

        self.colocar_minas()
   def colocar_minas(self):
        minas_colocadas = 0
        while minas_colocadas < NUM_MINAS:
            fila = random.randint(0, NUM_FILAS - 1)
            columna = random.randint(0, NUM_COLUMNAS - 1)
            if self.tablero[fila][columna]["text"] != "M":
                self.tablero[fila][columna]["text"] = "M"
                minas_colocadas += 1

    def abrir_casilla(self, fila, columna):
        if self.tablero[fila][columna]["text"] == "M":
            self.tablero[fila][columna]["text"] = "X"
        else:
            self.tablero[fila][columna]["text"] = " "

def main():
    root = tk.Tk()
    buscaminas = Buscaminas(root)
    root.mainloop()

if __name__ == '__main__':
    main()




