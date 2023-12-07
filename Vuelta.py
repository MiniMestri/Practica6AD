import tkinter as tk
import random


class Objetos:
    def __init__(self):
        self.posx = random.randint(0,1024)
        self.posy = random.randint(0,1024)
        self.radioS = 30
        self.radioM = 300
        self.direccion = random.randint(0,360)
        self.color = "blue"
        self.entidad=""
        
raiz=tk.Tk()

#Creo lienzo
lienzo=tk.Canvas(width=1024,height=1024)
lienzo.pack()

raiz.mainloop()
