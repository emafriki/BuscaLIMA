import tkinter as tk
from tkinter import *
from tkinter import messagebox
import random
import time

ANCHO, ALTO, CANTIDAD_BOMBAS = 6, 6, 6

root = Tk()
frame = Frame(root)
frame.pack()
root.title("Buscaminas")
root.iconbitmap("img/bomba.ico")
root.resizable(False, False)
frame.config(width=400, height=400)

def crear_menu():
    menu_bar = Menu(frame)
    root.config(menu=menu_bar)

    menu_dificultad = Menu(menu_bar, tearoff=0)
    menu_bar.add_cascade(label="Dificultad", menu=menu_dificultad)
    menu_dificultad.add_command(label="Fácil", command=lambda: establecer_dificultad(6, 6, 6))
    menu_dificultad.add_command(label="Intermedio", command=lambda: establecer_dificultad(8, 8, 8))
    menu_dificultad.add_command(label="Difícil", command=lambda: establecer_dificultad(10, 10, 10))

def establecer_dificultad(ancho, alto, cantidad_bombas):
    global ANCHO, ALTO, CANTIDAD_BOMBAS
    ANCHO, ALTO, CANTIDAD_BOMBAS = ancho, alto, cantidad_bombas
    limpiar_tablero()
    crear_tablero()

def limpiar_tablero():
    global botones
    for i in range(len(botones)):
        for j in range(len(botones[i])):
            if botones[i][j] is not None:
                botones[i][j].unbind("<Button-3>")
                botones[i][j].destroy()
                botones[i][j] = None

def crear_tablero():
    global tablero, botones, banderas
    tablero = [[0] * ANCHO for _ in range(ALTO)]
    banderas = [[False] * ANCHO for _ in range(ALTO)]
    place_bombs()
    calculate_numbers()

    botones = [[None] * ANCHO for _ in range(ALTO)]

    for i in range(ALTO):
        for j in range(ANCHO):
            botones[i][j] = Button(frame, text="", width=6, height=3, font=("Arial 12 bold"),
                                      command=lambda i=i, j=j: on_left_click(i, j))
            botones[i][j].bind("<Button-3>", lambda event, i=i, j=j: on_right_click(i, j))
            botones[i][j].grid(row=i, column=j)

def place_bombs():
    bombs_placed = 0
    while bombs_placed < CANTIDAD_BOMBAS:
        x, y = random.randint(0, ANCHO - 1), random.randint(0, ALTO - 1)
        if tablero[y][x] != -1:
            tablero[y][x] = -1
            bombs_placed += 1

def calculate_numbers():
    for i in range(ALTO):
        for j in range(ANCHO):
            if tablero[i][j] == -1:
                continue
            for x in range(-1, 2):
                for y in range(-1, 2):
                    if 0 <= i + y < ALTO and 0 <= j + x < ANCHO and tablero[i + y][j + x] == -1:
                        tablero[i][j] += 1


def on_left_click(i, j):
    if tablero[i][j] == -1:
        game_over()
    elif tablero[i][j] == 0:
        reveal_empty_cells(i, j)
    else:
        botones[i][j].config(text=str(tablero[i][j]))

def on_right_click(i, j):
    if botones[i][j]["state"] == tk.NORMAL:
        if not banderas[i][j]:
            botones[i][j].config(text="🚩", fg="red")
            banderas[i][j] = True
        else:
            botones[i][j].config(text="")
            banderas[i][j] = False

def reveal_empty_cells(i, j):
    if 0 <= i < ALTO and 0 <= j < ANCHO and botones[i][j]["state"] == tk.NORMAL:
        if tablero[i][j] == 0:
            botones[i][j].config(state=tk.DISABLED, text="")
            for x in range(-1, 2):
                for y in range(-1, 2):
                    reveal_empty_cells(i + y, j + x)

        elif 0 < tablero[i][j] < 9:
            botones[i][j].config(state=tk.DISABLED, text=str(tablero[i][j]))

imagenBomba=PhotoImage(file="img/bomba3.png")

def game_over():
    for i in range(ALTO):
        for j in range(ANCHO):
            if tablero[i][j] == -1:
                botones[i][j].config(image=imagenBomba, width=64, height=65, bg="#f17070", state=tk.DISABLED)
            else:
                botones[i][j].config(state=tk.DISABLED)
    respuesta = messagebox.askyesno("Fin del Juego", "¡Has perdido!\n¿Quieres volver a jugar?")
    if respuesta==True:
        reiniciar_juego()
    else:
        root.destroy()

def reiniciar_juego():
    for i in range(ALTO):
        for j in range(ANCHO):
            botones[i][j].config(state=tk.NORMAL, text="")
            banderas[i][j] = False
    crear_tablero()
    
if __name__ == "__main__":
    crear_menu()
    crear_tablero()
    root.mainloop()
