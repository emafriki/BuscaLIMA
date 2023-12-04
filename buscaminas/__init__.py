from tkinter import *
from tkinter import messagebox
import tkinter as tk
import random
import time


root=Tk()
frame=Frame(root)
frame.pack()
root.title("Buscaminas")
root.iconbitmap("img/bomba.ico")
root.resizable(False, False)
frame.config(width=400, height=400)
#--------------Variables--------------
bombasCerca=0
win=False
listaBotones=[]
reset=False
inicio=False
varSlotPulsado=-1
banderasDisponibles=10
tiempoFin=0
tiempoActual=0
tiempoInicio=time.time()
bandera=False
tiempoHabilitado=False
tomarTiempoFin=0
y=0

contadorTiempo=Label(frame)
contadorTiempo.grid(column=1, row=0, columnspan=4)

#------------Contador del tiempo-------------------
def tiempo(tiempo1=""):
	if tiempo1!=tiempo2 and tiempoHabilitado==True:
		tiempo1=tiempo2
		tiempoActual=int(tiempo2-tiempoInicio)
		contadorTiempo.config(text="Tiempo transcurrido: " + str(tiempoActual), font=("Arial 15"))
	else:
		tiempo1=tiempo2
		y+=1
		if y==1:
			tomarTiempoFin=int(tiempo2-tiempoInicio)
			print("termino en: ", tomarTiempoFin)
		contadorTiempo.config(text="Tiempo transcurrido: " + str(tomarTiempoFin), font=("Arial 15"))
	contadorTiempo.after(200, tiempo)
  
#-------Generacion del tablero-------

def generarBotones():
            for c in range(81): 
		    
                 listaBotones.append(Button(frame, width=6, height=3, text=" ", font=("Arial 12 bold"), command=lambda c=c:slotPulsado(c), bg="grey"))
    


