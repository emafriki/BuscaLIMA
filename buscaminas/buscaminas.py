from tkinter import *
from tkinter import messagebox
import tkinter as tk
import random
import time


root = Tk()
frame = Frame(root)
frame.pack()
root.title("Buscaminas")
root.iconbitmap("../img/bomba.ico")
root.resizable(False, False)
frame.config(width=400, height=400)
#--------------Variables--------------
bombasCerca = 0 
win = False
listaBotones = []
reset = False
inicio = False
varSlotPulsado = -1
banderasDisponibles = 10
tiempoFin = 0
tiempoActual = 0
tiempoInicio = time.time()
bandera = False
tiempoHabilitado = False
tomarTiempoFin = 0
y = 0

contadorTiempo = Label(frame)
contadorTiempo.grid(column = 1, row = 0, columnspan = 4)

#------------Contador del tiempo-------------------
def tiempo(tiempo1=""):
    """ Funcion para el contador de tiempo """
    global tiempoInicio, tiempoActual, inicio, tomarTiempoFin, tiempoHabilitado, y
    tiempo2 = time.time()
    if tiempo1 != tiempo2 and tiempoHabilitado:
        tiempo1 = tiempo2
        tiempoActual = int(tiempo2 - tiempoInicio)
    else:
        tiempo1 = tiempo2
        y += 1
        if y == 1:
            tomarTiempoFin = int(tiempo2 - tiempoInicio)
            print("termino en:", tomarTiempoFin)
    contadorTiempo.config(text="Tiempo transcurrido: " + str(tiempoActual if tiempoHabilitado else tomarTiempoFin),
                          font=("Arial 15"))
    contadorTiempo.after(200, tiempo)

#-------Generacion del tablero-------

def generarBotones():
    """ Funcion para el generar el tablero"""
    global listaBotones
    rows, columns = 9, 9
    button_width, button_height = 6, 3 	
    for c in range(rows * columns):
        row_position = (c // columns) + 1
        col_position = (c % columns) + 1
        button = Button(frame, width=button_width, height=button_height, text=" ", font=("Arial 12 bold"),
                        command=lambda c=c: slotPulsado(c), bg="grey")
        button.grid(column=col_position, row=row_position)
        listaBotones.append(button)

generarBotones()
#---------------Bombas---------------
bombas = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1]

def bombasRandom():
    global bombas
    bombas = []
    while len(bombas) < 10:  
        posicion = random.randrange(81)
        if posicion not in bombas:  
            bombas.append(posicion)

bombasRandom()

numeroPulsaciones=0
imagenBomba = root.iconbitmap("../img/bomba.ico")

def mostrarBombas():
    global imagenBomba
    for bomba in bombas:
        if bomba != -1:
            listaBotones[bomba].config(image=imagenBomba, width=64, height=65)
            	
   def slot_pulsado(slot):
        global bombas, listaBotones, bombasCerca, numeroPulsaciones, imagenbomba, win, reset, 
            varSlotPulsado, inicio, bandera, tiempoHabilitado, tomarTiempoFin, contadorTiempo, tiempoFin, tiempo2, 
            tiempoInicio, banderasDisponibles, bandera_img_slot, bandera_img, tiempoActual

    numeroPulsaciones += 1
    bombasCerca = 0
    varSlotPulsado = slot
    tiempoHabilitado = True

    if varSlotPulsado == -1:
        pass
    else:
        inicio = True
        tiempo()

    if not win:
        if slot in bombas:
            if bandera:
                poner_bandera()
            else:
                mostrar_bombas()
                lista_botones[slot].config(image=imagen_bomba, width=64, height=65, bg="#f17070")
                tiempoHabilitado = False
                reset = messagebox.askyesno("Game Over", "¿Desea volver a jugar?")
                game_reset()
        else:
            def check():
                nonlocal bombasCerca
                neighbors = [slot + 1, slot - 1, slot + 9, slot - 9, slot - 8, slot + 8, slot + 10, slot - 10]
                bombasCerca += sum(1 for neighbor in neighbors if neighbor in bombas)
                print("abajo" if slot + 1 in bombas else "",
                      "arriba" if slot - 1 in bombas else "",
                      "derecha" if slot + 9 in bombas else "",
                      "izquierda" if slot - 9 in bombas else "",
                      "abajo a la izquierda" if slot - 8 in bombas else "",
                      "arriba a la derecha" if slot + 8 in bombas else "",
                      "abajo a la derecha" if slot + 10 in bombas else "",
                      "arriba a la izquierda" if slot - 10 in bombas else "")

            check()

            if not bandera:
                lista_botones[slot].config(text=bombas_cercanas, fg="black", font=("Arial 12 bold"))
                lista_botones[slot].config(bg="#aeb0b2", state="disabled")
            else:
                poner_bandera()

            def check_win():
                nonlocal win
                if slot not in bombas and numeroPulsaciones == 71:
                    win = True
                    txt_win = Label(frame, width=25, height=2, text="¡ G A N A S T E !", font=("helvetica 27 bold"), bg="#fe4a4a")
                    txt_win.grid(row=10, column=1, columnspan=9)
                    frame.config(bg="#fe4a4a")
                    contadorTiempo.config(bg="#fe4a4a")
                mostrar_bombas()

            check_win()
def presionar_bandera():
    global bandera
    bandera = True

def poner_bandera():
    global var_slot_pulsado, bandera, banderas_disponibles, contador_banderas, lista_botones, bandera_img_slot
    if bandera and banderas_disponibles > 0:
        banderas_disponibles -= 1
        contador_banderas.config(text="Banderas disponibles: " + str(banderas_disponibles))
        lista_botones[var_slot_pulsado].config(image=bandera_img_slot, width=64, height=65)
        print("Bandera puesta en: ", var_slot_pulsado)
    bandera = False

contador_banderas = Label(frame, text="Banderas disponibles: " + str(banderas_disponibles), font=("Arial 15"))
contador_banderas.grid(column=6, row=0, columnspan=5)

boton_bandera = Button(frame, text=" ", image=bandera_img, command=presionar_bandera)
boton_bandera.grid(column=5, row=0)

def game_reset():
    global reset, bombas_cercanas, win, lista_botones, tiempo_actual, tiempo_inicio, tiempo1, tiempo2, tiempo_actual, banderas_disponibles, bandera, y, tomar_tiempo_fin, tiempo_habilitado, numero_pulsaciones
    if reset:
        comienzo = False
        bombas_cercanas = 0
        win = False
        lista_botones = []
        bombas = [random.randrange(81) for _ in range(10)]
        print("Las ubicaciones de las bombas son:", bombas)
        numero_pulsaciones = 0
        bombas_cercanas = 0
        generar_botones()
        tiempo_inicio = time.time()
        tiempo()
        banderas_disponibles = 10
        contador_banderas.config(text="Banderas disponibles: " + str(banderas_disponibles))
        bandera = False
        reset = False
    else:
        root.destroy()

# loop
root.mainloop()


		
    


