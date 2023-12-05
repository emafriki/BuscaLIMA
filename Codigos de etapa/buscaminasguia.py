from tkinter import *
from tkinter import messagebox
import tkinter as tk
import random
import time


root=Tk()
frame=Frame(root)
frame.pack()
root.title("Buscaminas")
icono = tk.PhotoImage(file="https://github.com/emafriki/BuscaLIMA/blob/main/img/bomba.ico")
root.iconphoto(True, icono)
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

def tiempo(tiempo1=""):
	global tiempoInicio, tiempoActual, inicio, tomarTiempoFin, tiempoHabilitado, y, tiempo2
	tiempo2=time.time()
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

def generarBotones():
	global listaBotones
	for c in range(81):
		listaBotones.append(Button(frame, width=6, height=3, text=" ", font=("Arial 12 bold"), command=lambda c=c:slotPulsado(c), bg="grey"))
		if c >= 0 and c < 9:
			listaBotones[c].grid(column=1, row=c+1)
		if c >= 9 and c < 18:
			listaBotones[c].grid(column=2, row=c-8)
		if c >= 18 and c < 27:
			listaBotones[c].grid(column=3, row=c-17)
		if c >= 27 and c < 36:
			listaBotones[c].grid(column=4, row=c-26)
		if c >= 36 and c < 45:
			listaBotones[c].grid(column=5, row=c-35)
		if c >= 45 and c < 54:
			listaBotones[c].grid(column=6, row=c-44)
		if c >= 54 and c < 63:
			listaBotones[c].grid(column=7, row=c-53)
		if c >= 63 and c < 72:
			listaBotones[c].grid(column=8, row=c-62)
		if c >= 72 and c < 81:
			listaBotones[c].grid(column=9, row=c-71)
generarBotones()
#---------------Bombas---------------
bomba1=-1
bomba2=-1
bomba3=-1
bomba4=-1
bomba5=-1
bomba6=-1
bomba7=-1
bomba8=-1
bomba9=-1
bomba10=-1

def bombasRandom():
	global bomba1, bomba2, bomba3, bomba4, bomba5, bomba6, bomba7, bomba8, bomba9, bomba10
	bomba1=random.randrange(81)
	bomba2=random.randrange(81)
	bomba3=random.randrange(81)
	bomba4=random.randrange(81)
	bomba5=random.randrange(81)
	bomba6=random.randrange(81)
	bomba7=random.randrange(81)
	bomba8=random.randrange(81)
	bomba9=random.randrange(81)
	bomba10=random.randrange(81)
bombasRandom()

print("Las ubicaciones de las bombas son: ", bomba1, bomba2, bomba3, bomba4, bomba5, bomba6, bomba7, bomba8, bomba9, bomba10)

numeroPulsaciones=0
imagenBomba=PhotoImage(file='/home/aamyf/EmafrikiO/img/bomba3.png')

def mostrarBombas():
	global imagenBomba
	listaBotones[bomba1].config(image=imagenBomba, width=64, height=65)
	listaBotones[bomba2].config(image=imagenBomba, width=64, height=65)
	listaBotones[bomba3].config(image=imagenBomba, width=64, height=65)
	listaBotones[bomba4].config(image=imagenBomba, width=64, height=65)
	listaBotones[bomba5].config(image=imagenBomba, width=64, height=65)
	listaBotones[bomba6].config(image=imagenBomba, width=64, height=65)
	listaBotones[bomba7].config(image=imagenBomba, width=64, height=65)
	listaBotones[bomba8].config(image=imagenBomba, width=64, height=65)
	listaBotones[bomba9].config(image=imagenBomba, width=64, height=65)
	listaBotones[bomba10].config(image=imagenBomba, width=64, height=65)

def slotPulsado(slot):
	global bomba1, bomba2, bomba3, bomba4, bomba5, bomba6, bomba7, bomba8, bomba9, bomba10, listaBotones, bombasCerca, numeroPulsaciones, imagenBomba, win, reset, varSlotPulsado, inicio, ponerBandera, bandera, tiempoHabilitado, tomarTiempoFin, contadorTiempo, tiempoFin, tiempo2, tiempoInicio
	numeroPulsaciones+=1
	bombasCerca=0
	varSlotPulsado=slot
	tiempoHabilitado=True

	if slotPulsado == -1:
		pass
	else:
		inicio=True
		tiempo()

	if win!=True:
		if slot == bomba1 or slot == bomba2 or slot == bomba3 or slot == bomba4 or slot == bomba5 or slot == bomba6 or slot == bomba7 or slot == bomba8 or slot == bomba9 or slot == bomba10:
			if bandera==True:
				ponerBandera()
			else:
				mostrarBombas()
				listaBotones[slot].config(image=imagenBomba, width=64, height=65, bg="#f17070")
				tiempoHabilitado=False
				#----reset----
				reset=messagebox.askyesno("Game Over", "¿Desea volver a jugar?")
				gameReset()
		else:
			def check():
				global bombasCerca
				if slot+1==bomba1 or slot+1==bomba2 or slot+1==bomba3 or slot+1==bomba4 or slot+1==bomba5 or slot+1==bomba6 or slot+1==bomba7 or slot+1==bomba8 or slot+1==bomba9 or slot+1==bomba10:
					bombasCerca+=1
					print("abajo")
				if slot-1==bomba1 or slot-1==bomba2 or slot-1==bomba3 or slot-1==bomba4 or slot-1==bomba5 or slot-1==bomba6 or slot-1==bomba7 or slot-1==bomba8 or slot-1==bomba9 or slot-1==bomba10:
					bombasCerca+=1
					print("arriba")
				if slot+9==bomba1 or slot+9==bomba2 or slot+9==bomba3 or slot+9==bomba4 or slot+9==bomba5 or slot+9==bomba6 or slot+9==bomba7 or slot+9==bomba8 or slot+9==bomba9 or slot+9==bomba10:
					bombasCerca+=1
					print("derecha")
				if slot-9==bomba1 or slot-9==bomba2 or slot-9==bomba3 or slot-9==bomba4 or slot-9==bomba5 or slot-9==bomba6 or slot-9==bomba7 or slot-9==bomba8 or slot-9==bomba9 or slot-9==bomba10:
					bombasCerca+=1
					print("izquierda")
				if slot-8==bomba1 or slot-8==bomba2 or slot-8==bomba3 or slot-8==bomba4 or slot-8==bomba5 or slot-8==bomba6 or slot-8==bomba7 or slot-8==bomba8 or slot-8==bomba9 or slot-8==bomba10:
					bombasCerca+=1
					print("abajo a la izquierda")
				if slot+8==bomba1 or slot+8==bomba2 or slot+8==bomba3 or slot+8==bomba4 or slot+8==bomba5 or slot+8==bomba6 or slot+8==bomba7 or slot+8==bomba8 or slot+8==bomba9 or slot+8==bomba10:
					bombasCerca+=1
					print("arriba a la derecha")
				if slot+10==bomba1 or slot+10==bomba2 or slot+10==bomba3 or slot+10==bomba4 or slot+10==bomba5 or slot+10==bomba6 or slot+10==bomba7 or slot+10==bomba8 or slot+10==bomba9 or slot+10==bomba10:
					bombasCerca+=1
					print("abajo a la derecha")
				if slot-10==bomba1 or slot-10==bomba2 or slot-10==bomba3 or slot-10==bomba4 or slot-10==bomba5 or slot-10==bomba6 or slot-10==bomba7 or slot-10==bomba8 or slot-10==bomba9 or slot-10==bomba10:
					bombasCerca+=1
					print("arriba a la izquierda")
			check()
			
			if bandera==False:
				listaBotones[slot].config(text=bombasCerca, fg="black", font=("Arial 12 bold"))
				listaBotones[slot].config(bg="#aeb0b2", state="disabled")
			else:
				ponerBandera()

			def checkWin():
				global imagenBomba, listaBotones, win, contadorBanderas
				if slot != bomba1 and slot != bomba2 and slot != bomba3 and slot != bomba4 and slot != bomba5 and slot != bomba6 and slot != bomba7 and slot != bomba8 and slot != bomba9 and slot != bomba10 and numeroPulsaciones == 71:
					win=True
					txtWin1=Label(frame, width=25, height=2, text="¡  G  A  N  A  S  T  E  !", font=("helvetica 27 bold"), bg="#fe4a4a")
					txtWin1.grid(row=10, column=1, columnspan=9)
					frame.config(bg="#fe4a4a")
					contadorBanderas.config(bg="#fe4a4a")
					contadorTiempo.config(bg="#fe4a4a")
					mostrarBombas()
			checkWin()

#-------------Banderas----------
def presionarBandera():
	global bandera
	bandera=True
banderaImg=PhotoImage(file='/home/aamyf/EmafrikiO/img/bandera.png')
banderaImgSlot=PhotoImage(file='/home/aamyf/EmafrikiO/img/banderaSlot.png')
def ponerBandera():
	global varSlotPulsado, bandera, banderasDisponibles, contadorBanderas, botonBandera, listaBotones
	if bandera and banderasDisponibles>0:
		banderasDisponibles=banderasDisponibles-1
		contadorBanderas.config(text="Banderas disponibles: " + str(banderasDisponibles))
		listaBotones[varSlotPulsado].config(image=banderaImgSlot, width=64, height=65)
		print("Bandera puesta en: ", varSlotPulsado)
	bandera=False

contadorBanderas=Label(frame, text="Banderas disponibles: " + str(banderasDisponibles), font=("Arial 15"))
contadorBanderas.grid(column=6, row=0, columnspan=5)

botonBandera=Button(frame, text=" ", image=banderaImg, command=lambda:presionarBandera())
botonBandera.grid(column=5, row=0)

#----------Game Reset-----------
def gameReset():
	global reset, bombasCerca, win, listaBotones, tiempoActual, tiempoInicio, tiempo1, tiempo2, tiempoActual, banderasDisponibles, bandera, y, tomarTiempoFin, tiempoHabilitado
	if reset==True:
		comienzo=False
		bombasCerca=0
		win=False
		listaBotones=[]
		bomba1=-1
		bomba2=-1
		bomba3=-1
		bomba4=-1
		bomba5=-1
		bomba6=-1
		bomba7=-1
		bomba8=-1
		bomba9=-1
		bomba10=-1
		tomarTiempoFin=0
		y=0
		tiempoActual=0
		tiempoHabilitado==False
		bombasRandom()
		numeroPulsaciones=0
		bombasCerca=0
		generarBotones()
		tiempoInicio=time.time()
		tiempo()
		banderasDisponibles=10
		contadorBanderas.config(text="Banderas disponibles: " + str(banderasDisponibles))
		bandera=False
		reset=False
	else:
		root.destroy()
#loop-----------
root.mainloop()
