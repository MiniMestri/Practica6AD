import tkinter as tk
import random
import math

objetos=[]
numerosats=5


class Objetos:
    def __init__(self):
        self.centrox = 512
        self.centroy = 512
        self.radioS = 30
        self.radioM = 300
        self.direccion = random.randint(0,360)
        self.color1 = "blue"
        self.color2 = "green"
        self.color3="grey"
        self.grosorborde=10
        self.entidad=""
        self.velocidad = random.randint(1,5)
        self.angulo=random.randint(0,360)
        self.a=random.randint(1,5)
        self.b=random.randint(1,5)
    def visualizarT(self):
        lienzo.create_oval(
            self.centrox-self.radioM/2,
            self.centroy-self.radioM/2,
            self.centrox+self.radioM/2,
            self.centroy+self.radioM/2,
            fill=self.color1,
            outline=self.color2,
            width=self.grosorborde)
    def visualizarS(self):
        self.entidad=lienzo.create_oval(
            self.centrox-self.radioS/2,
            self.centroy-self.radioS/2,
            self.centrox+self.radioS/2,
            self.centroy+self.radioS/2,
            fill=self.color3)
    def mueve(self):
        self.angulo += math.radians(self.velocidad)
        x = self.centrox + self.a * math.cos(self.angulo)
        y = self.centroy + self.b * math.sin(self.angulo)
        lienzo.move(self.entidad, x - self.centrox, y - self.centroy)
        self.centrox, self.centroy = x, y
        
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

def velocidad():    
    for objeto in objetos:
        objeto.mueve()
    raiz.after(10,velocidad)

print(objetos)
velocidad()

raiz.mainloop()
