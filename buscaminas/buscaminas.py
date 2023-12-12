import tkinter as tk
from tkinter import *
from tkinter import messagebox
import random
import time

WIDTH, HEIGHT, BOMB_COUNT = 6, 6, 6

root = Tk()
frame = Frame(root)
frame.pack()
root.title("Buscaminas")
root.iconbitmap("img/bomba.ico")
root.resizable(False, False)
frame.config(width=400, height=400)

# Time counter
time_start = 0
time_label = None
time_active = True

"""A funcion that time starter"""

def start_time():
    global time_start
    time_start = time.time()
    update_time()

"""A funcion that updates the time"""

def update_time():
    global time_active
    if time_active:
        time_elapsed = round(time.time() - time_start)
        time_label.config(text=f"Tiempo: {time_elapsed}s")
        root.after(1000, update_time)

"""A function that creates the game levels"""

def create_menu():
    menu_bar = Menu(frame)
    root.config(menu=menu_bar)

    difficulty_menu = Menu(menu_bar, tearoff=0)
    menu_bar.add_cascade(label="Dificultad", menu=difficulty_menu)
    difficulty_menu.add_command(label="Facil", command=lambda: set_difficulty(6, 6, 6))
    difficulty_menu.add_command(label="Intermedio", command=lambda: set_difficulty(7, 7, 8))
    difficulty_menu.add_command(label="Dificil", command=lambda: set_difficulty(9, 9, 10))
