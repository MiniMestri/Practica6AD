import tkinter as tk
import random

objetos=[]
numerobjetos=1

class Objetos:
    def __init__(self):
        self.posx = 512
        self.posy = 512
        self.radioS = 30
        self.radioM = 300
        self.direccion = random.randint(0,360)
        self.color1 = "blue"
        self.color2 = "green"
        self.grosorborde=10
        self.entidad=""
    def visualizar(self):
        self.entidad=lienzo.create_oval(
            self.posx-self.radioM/2,
            self.posy-self.radioM/2,
            self.posx+self.radioM/2,
            self.posy+self.radioM/2,
            fill=self.color1,
            outline=self.color2,
            width=self.grosorborde)
        
raiz=tk.Tk()

#Creo lienzo
lienzo=tk.Canvas(width=1024,height=1024)
lienzo.pack()

objeto=Objetos()
objeto.visualizar()

raiz.mainloop()
