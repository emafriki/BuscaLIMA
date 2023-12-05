from tkinter import *
from tkinter import messagebox
import random
import time

root = Tk()
root.title("Buscaminas")
root.iconbitmap("img/bomba.ico")
root.resizable(False, False)

frame = Frame(root, width=400, height=400)
frame.pack()

bombas_cercanas = 0
win = False
lista_botones = []
reset = False
inicio = False
var_slot_pulsado = -1
banderas_disponibles = 10
tiempo_fin = 0
tiempo_actual = 0
tiempo_inicio = time.time()
bandera = False
tiempo_habilitado = False
tomar_tiempo_fin = 0
y = 0

contador_tiempo = Label(frame)
contador_tiempo.grid(column=1, row=0, columnspan=4)

imagen_bomba = PhotoImage(file="img/bomba3.png")
bandera_img = PhotoImage(file="img/bandera.png")
bandera_img_slot = PhotoImage(file="img/banderaSlot.png")

def tiempo(tiempo1=""):
    global tiempo_inicio, tiempo_actual, inicio, tomar_tiempo_fin, tiempo_habilitado, y, tiempo2
    tiempo2 = time.time()
    if tiempo1 != tiempo2 and tiempo_habilitado:
        tiempo1 = tiempo2
        tiempo_actual = int(tiempo2 - tiempo_inicio)
        contador_tiempo.config(text="Tiempo transcurrido: " + str(tiempo_actual), font=("Arial 15"))
    else:
        tiempo1 = tiempo2
        y += 1
        if y == 1:
            tomar_tiempo_fin = int(tiempo2 - tiempo_inicio)
            print("termino en: ", tomar_tiempo_fin)
        contador_tiempo.config(text="Tiempo transcurrido: " + str(tomar_tiempo_fin), font=("Arial 15"))
    contador_tiempo.after(200, tiempo)

def generar_botones():
    global lista_botones
    for c in range(81):
        button = Button(frame, width=6, height=3, text=" ", font=("Arial 12 bold"), command=lambda c=c: slot_pulsado(c), bg="grey")
        row, col = divmod(c, 9)
        button.grid(column=col+1, row=row+1)
        lista_botones.append(button)

generar_botones()

bombas = [random.randrange(81) for _ in range(10)]
print("Las ubicaciones de las bombas son:", bombas)

numero_pulsaciones = 0

def mostrar_bombas():
    global imagen_bomba
    for bomba in bombas:
        lista_botones[bomba].config(image=imagen_bomba, width=64, height=65)

def slot_pulsado(slot):
    global bombas, lista_botones, bombas_cercanas, numero_pulsaciones, imagen_bomba, win, reset, var_slot_pulsado, inicio, bandera, tiempo_habilitado, tomar_tiempo_fin, contador_tiempo, tiempo_fin, tiempo2, tiempo_inicio
    numero_pulsaciones += 1
    bombas_cercanas = 0
    var_slot_pulsado = slot
    tiempo_habilitado = True

    if var_slot_pulsado == -1:
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
                tiempo_habilitado = False
                reset = messagebox.askyesno("Game Over", "¿Desea volver a jugar?")
                game_reset()
        else:
            def check():
                nonlocal bombas_cercanas
                neighbors = [slot + 1, slot - 1, slot + 9, slot - 9, slot - 8, slot + 8, slot + 10, slot - 10]
                bombas_cercanas += sum(1 for neighbor in neighbors if neighbor in bombas)
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
                if slot not in bombas and numero_pulsaciones == 71:
                    win = True
                    txt_win = Label(frame, width=25, height=2, text="¡ G A N A S T E !", font=("helvetica 27 bold"), bg="#fe4a4a")
                    txt_win.grid(row=10, column=1, columnspan=9)
                    frame.config(bg="#fe4a4a")
                    contador_tiempo.config(bg="#fe4a4a")
                mostrar_bombas()

            check_win()

def presionar_bandera():
    global bandera
    bandera = True

def poner_bandera():
    global var_slot_pulsado, bandera, banderas_disponibles, contador_banderas, lista_botones
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
    global reset, bombas_cercanas, win, lista_botones, tiempo_actual, tiempo_inicio, tiempo1, tiempo2, tiempo_actual, banderas_disponibles, bandera, y, tomar_tiempo_fin, tiempo_habilitado
    if reset:
        comienzo = False
        bombas
