import tkinter as tk
from tkinter import *
from tkinter import messagebox
import random
import time

#-----------------Dashboard Generator----------------

#Default level (easy)
WIDTH, HEIGHT, BOMB_COUNT = 6, 6, 6

root = Tk()
frame = Frame(root)
frame.pack()
root.title("Buscaminas")
root.iconbitmap("img/bomba.ico")
root.resizable(False, False)
frame.config(width=400, height=400)


#-----------------Time counter----------------


#Variables
time_start = 0
time_label = None
time_active = True

def start_time():
    """ This function starts the time for the counter """
    global time_start
    time_start = time.time()
    update_time()

def update_time():
    """ This function updates the time every time you restart or change levels """
    global time_active
    if time_active:
        time_elapsed = round(time.time() - time_start)
        time_label.config(text=f"Tiempo: {time_elapsed}s")
        root.after(1000, update_time)


#-----------------Dropdown menu----------------

def create_menu():
    """ This function creates the dropdown menu to choose between three levels """
    menu_bar = Menu(frame)
    root.config(menu=menu_bar)

    difficulty_menu = Menu(menu_bar, tearoff=0)
    menu_bar.add_cascade(label="Dificultad", menu=difficulty_menu)
    difficulty_menu.add_command(label="Facil", command=lambda: set_difficulty(6, 6, 6))
    difficulty_menu.add_command(label="Intermedio", command=lambda: set_difficulty(7, 7, 8))
    difficulty_menu.add_command(label="Dificil", command=lambda: set_difficulty(9, 9, 10))

















#-------------------------------------Reveal empty cells-------------------------------------


def reveal_empty_cells(i, j, visited):
    """ Function that reveals the cells where there is a zero or better known as empty cells """
    if (0 <= i < HEIGHT and 0 <= j < WIDTH and
            buttons[i][j]["state"] == tk.NORMAL and
            (i, j) not in visited):
        visited.add((i, j))
        if board[i][j] == 0:
            buttons[i][j].config(state=tk.DISABLED, text="")
            for x in range(-1, 2):
                for y in range(-1, 2):
                    reveal_empty_cells(i + y, j + x, visited)
        elif 0 < board[i][j] < 9:
            buttons[i][j].config(state=tk.DISABLED, text=str(board[i][j]))


#-------------------------------------Win-------------------------------------

def check_win():
    """ Function that verifies if you have won """
    cells_without_bomb = [buttons[i][j]["state"] == tk.DISABLED for i in range(HEIGHT) for j in range(WIDTH)]
    if all(cells_without_bomb):
        messagebox.showinfo("¡Felicidades!", f"¡Has ganado!")
    response = messagebox.askyesno("Fin del Juego", f"¡Has perdido!\n¿Quieres volver a jugar?")
    if response:
        restart_game()
    else:
        root.destroy()


#-------------------------------------Game Over-------------------------------------

imagenBomba= PhotoImage(file="img/bomba3.png") #Definimos la imagen de la bomba que deseemos que se muestra

def game_over():
    """ Function that indicates when you lose """"
    global time_active
    time_active = False

    for i in range(HEIGHT):
        for j in range(WIDTH):
            if board[i][j] == -1:
                buttons[i][j].config(image=imagenBomba, width=64, height=65, bg="#f17070")
            else:
                buttons[i][j].config(state=tk.DISABLED) 
    response = messagebox.askyesno("Fin del Juego", f"¡Has perdido!\n¿Quieres volver a jugar?") #Shows you a message to know if you want to play
    if response:
        restart_game()
    else:
        root.destroy()


#-----------------------------Reset game-------------------------

def restart_game():
    """ Function to restart the game """
    global time_active
    time_active = True  # Reactivate the timer
    clear_board()
    create_board()
    start_time()  # Start the timer again


#-----------Shows the graphical interface of the game-------

if __name__ == "__main__":
    create_menu()
    create_board()
    root.mainloop()

