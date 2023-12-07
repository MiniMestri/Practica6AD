import tkinter as tk
import random
import math

objetos=[]
numerosats=5
velocidades=random.randint(0,100)

class Objetos:
    def __init__(self):
        self.posx = 512
        self.posy = 512
        self.radioS = 30
        self.radioM = 300
        self.direccion = random.randint(0,360)
        self.color1 = "blue"
        self.color2 = "green"
        self.color3="grey"
        self.grosorborde=10
        self.entidad=""
    def visualizarT(self):
        lienzo.create_oval(
            self.posx-self.radioM/2,
            self.posy-self.radioM/2,
            self.posx+self.radioM/2,
            self.posy+self.radioM/2,
            fill=self.color1,
            outline=self.color2,
            width=self.grosorborde)
    def visualizarS(self):
        self.entidad=lienzo.create_oval(
            self.posx-self.radioS/2,
            self.posy-self.radioS/2,
            self.posx+self.radioS/2,
            self.posy+self.radioS/2,
            fill=self.color3)
    def mueve(self):
        lienzo.move(self.entidad,math.cos(self.direccion),math.sin(self.direccion))
        self.posx += math.cos(self.direccion)
        self.posy +=math.sin(self.direccion)

        
raiz=tk.Tk()

#Creo lienzo
lienzo=tk.Canvas(width=1024,height=1024)
lienzo.pack()

objeto=Objetos()
objeto.visualizarT()

for i in range(0,numerosats):
    objetos.append(Objetos())
    
for elemento in objetos:
    elemento.visualizarS()

def velocidad(velocidades):    
    for objeto in objetos:
        objeto.mueve()
    raiz.after(velocidades,velocidad)

bucle()

raiz.mainloop()
