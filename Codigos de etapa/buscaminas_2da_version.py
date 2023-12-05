import tkinter as tk
from tkinter import Button, Frame, Label, PhotoImage, messagebox
import random
import time

class Buscaminas:
    def __init__(self, root):
        self.root = root
        self.root.title("Buscaminas")
        self.root.iconphoto(True, PhotoImage(file="/home/aamyf/EmafrikiO/img/bomba.png"))
        self.root.resizable(False, False)

        self.frame = Frame(root)
        self.frame.pack()

        self.width = 400
        self.height = 400
        self.frame.config(width=self.width, height=self.height)

        self.bombas_cerca = 0
        self.win = False
        self.lista_botones = []
        self.reset = False
        self.inicio = False
        self.var_slot_pulsado = -1
        self.banderas_disponibles = 10
        self.tiempo_fin = 0
        self.tiempo_actual = 0
        self.tiempo_inicio = time.time()
        self.bandera = False
        self.tiempo_habilitado = False
        self.tomar_tiempo_fin = 0
        self.y = 0

        self.contador_tiempo = Label(self.frame)
        self.contador_tiempo.grid(column=1, row=0, columnspan=4)

        self.contador_banderas = Label(self.frame, text=f"Banderas disponibles: {self.banderas_disponibles}", font=("Arial 15"))
        self.contador_banderas.grid(column=6, row=0, columnspan=5)

        self.boton_bandera = Button(self.frame, text=" ", image=PhotoImage(file='/home/aamyf/EmafrikiO/img/bandera.png'), command=self.presionar_bandera)
        self.boton_bandera.grid(column=5, row=0)

        self.nivel_dificultad()

    def nivel_dificultad(self):
        nivel = messagebox.askquestion("Nivel de dificultad", "¿Selecciona el nivel de dificultad?\n(Fácil: 10 bombas, Medio: 20 bombas, Difícil: 30 bombas)")
        if nivel == "yes":
            self.generar_botones(10)
        elif nivel == "no":
            self.generar_botones(20)
        else:
            self.generar_botones(30)

    def tiempo(self, tiempo1=""):
        tiempo2 = time.time()
        if tiempo1 != tiempo2 and self.tiempo_habilitado:
            tiempo1 = tiempo2
            self.tiempo_actual = int(tiempo2 - self.tiempo_inicio)
            self.contador_tiempo.config(text=f"Tiempo transcurrido: {self.tiempo_actual}", font=("Arial 15"))
        else:
            tiempo1 = tiempo2
            self.y += 1
            if self.y == 1:
                self.tomar_tiempo_fin = int(tiempo2 - self.tiempo_inicio)
                print("termino en: ", self.tomar_tiempo_fin)
            self.contador_tiempo.config(text=f"Tiempo transcurrido: {self.tomar_tiempo_fin}", font=("Arial 15"))

        self.contador_tiempo.after(200, self.tiempo)

    def generar_botones(self, num_bombas):
        for c in range(81):
            row, col = divmod(c, 9)
            button = Button(self.frame, width=6, height=3, text=" ", font=("Arial 12 bold"), command=lambda c=c: self.slot_pulsado(c, num_bombas), bg="grey")
            button.grid(column=col + 1, row=row + 1)
            self.lista_botones.append(button)

        self.bombas_random(num_bombas)

    def bombas_random(self, num_bombas):
        self.bombas = random.sample(range(81), num_bombas)
        print("Las ubicaciones de las bombas son:", self.bombas)

    def mostrar_bombas(self):
        imagen_bomba = PhotoImage(file='/home/aamyf/EmafrikiO/img/bomba3.png')
        for bomba in self.bombas:
            self.lista_botones[bomba].config(image=imagen_bomba, width=64, height=65)

    def slot_pulsado(self, slot, num_bombas):
        self.bombas_cerca = 0
        self.var_slot_pulsado = slot
        self.tiempo_habilitado = True

        if not self.inicio:
            self.inicio = True
            self.tiempo()

        if not self.win:
            if slot in self.bombas:
                if self.bandera:
                    self.poner_bandera()
                else:
                    self.mostrar_bombas()
                    self.lista_botones[slot].config(image=PhotoImage(file='/home/aamyf/EmafrikiO/img/bomba3.png'), width=64, height=65, bg="#f17070")
                    self.tiempo_habilitado = False
                    reset = messagebox.askyesno("Game Over", "¿Desea volver a jugar?")
                    self.game_reset() if reset else self.root.destroy()
            elif self.bombas_cerca == 0:
                self.destapar_botones(slot, num_bombas)
            else:
                self.check(slot)

    def destapar_botones(self, slot, num_bombas):
        visited = set()
        to_check = [slot]

        while to_check:
            current_slot = to_check.pop()
            visited.add(current_slot)

            neighbors = [current_slot + 1, current_slot - 1, current_slot + 9, current_slot - 9, current_slot - 8, current_slot + 8, current_slot + 10, current_slot - 10]

            for neighbor in neighbors:
                if 0 <= neighbor < 81 and neighbor not in visited:
                    if neighbor not in self.bombas:
                        self.check(neighbor)
                        if self.bombas_cerca == 0:
                            to_check.append(neighbor)

    def check(self, slot):
        neighbors = [slot + 1, slot - 1, slot + 9, slot - 9, slot - 8, slot + 8, slot + 10, slot - 10]
        for neighbor in neighbors:
            if neighbor in self.bombas:
                self.bombas_cerca += 1

        if not self.bandera:
            self.lista_botones[slot].config(text=self.bombas_cerca, fg="black", font=("Arial 12 bold"))
            self.lista_botones[slot].config(bg="#aeb0b2", state="disabled")
        else:
            self.poner_bandera()

        self.check_win()

    def check_win(self):
        if self.var_slot_pulsado not in self.bombas and len(set(self.bombas) - set(self.lista_botones)) == 0:
            self.win = True
            txt_win = Label(self.frame, width=25, height=2, text="¡G A N A S T E!", font=("helvetica 27 bold"), bg="#fe4a4a")
            txt_win.grid(row=10, column=1, columnspan=9)
            self.frame.config(bg="#fe4a4a")
            self.contador_banderas.config(bg="#fe4a4a")
            self.contador_tiempo.config(bg="#fe4a4a")
            self.mostrar_bombas()

    def presionar_bandera(self):
        self.bandera = True

    def poner_bandera(self):
        if self.bandera and self.banderas_disponibles > 0:
            self.banderas_disponibles -= 1
            self.contador_banderas.config(text=f"Banderas disponibles: {self.banderas_disponibles}")
            self.lista_botones[self.var_slot_pulsado].config(image=PhotoImage(file='/home/aamyf/EmafrikiO/img/banderaSlot.png'), width=64, height=65)

    def game_reset(self):
        self.reset = True
        self.bombas_cerca = 0
        self.win = False
        self.lista_botones = []
        self.tomar_tiempo_fin = 0
        self.y = 0
        self.tiempo_actual = 0
        self.tiempo_habilitado == False
        self.bombas_random(10)
        self.numero_pulsaciones = 0
        self.bombas_cerca = 0
        self.generar_botones(10)
        self.tiempo_inicio = time.time()
        self.tiempo()
        self.banderas_disponibles = 10
        self.contador_banderas.config(text=f"Banderas disponibles: {self.banderas_disponibles}")
        self.bandera = False
        self.reset = False

root = tk.Tk()
buscaminas = Buscaminas(root)
root.mainloop()
