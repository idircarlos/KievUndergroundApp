import tkinter as tk
from tkinter import PhotoImage
from tkinter.constants import *
import tkinter.font as tkFont
import backend as bk
import database as db
import paradas as pds
from PIL import Image,ImageTk, ImageDraw
import rounded as rd
import coord_map as coord
import stop
import turtle as t

HEIGHT = 1000
WIDTH = 1000

""""
main_window = tk.Tk()
main_window.title("Metro Kiev")
main_window.geometry(str(HEIGHT) + "x" + str(WIDTH))
main_window.config(bg='white')
canvas = tk.Canvas(master = main_window, width = WIDTH, height = HEIGHT)
"""

""" Fuente del texto de la ruta """
#fontStyle = tkFont.Font(family="Lucida Grande", size=12)

""" Imagen del metro """
img = Image.open("./app/img/metrobien.png")
img = img.resize((900,900),Image.ANTIALIAS)
img.save("./app/img/metrobienresized.png")
#metro = ImageTk.PhotoImage(img)
#metro_canvas = tk.PhotoImage(file="./app/MetroKiev.png")
#canvas.create_image(0,0,image=metro_canvas,anchor="nw")
#canvas.pack()
#label = tk.Label(canvas,image=metro)
#label.place(x=70, y=90)

inicio = None
destino = None
pulsado = False

def draw_path(path):
    if path == None:
        print("Can't draw an empty path")
        return
    a.penup()
    a.speed(0)
    a.goto((path[0].coords[0], path[0].coords[1]))
    a.speed(2.5)
    for parada in path:
        a.pendown()
        a.goto(parada.coords[0],parada.coords[1])
        a.penup()




def printcoords(x,y):
    #outputting x and y coords to console
    global inicio, destino, pulsado, a
    print (x,y)
    #mouseclick event
    
    
    if pulsado == False:
        inicio = db.which_stop(x, y)
        if inicio is None:
            return
        print("Inicio: " + str(inicio))
        pulsado = True
    else:
        destino = db.which_stop(x, y)
        if destino is None:
            return
        print("Destino: " + str(destino))
        print()
        pulsado = False
        path = bk.a_estrella(inicio,destino)
        draw_path(path)
        return 
    
#main_window.bind("<Button 1>",printcoords)

win = t.Screen()
win.bgpic("./app/img/metrobienresized.png")
win.setup(height=HEIGHT, width=WIDTH)
win.title("Metro Kiev")
win.onclick(printcoords,1)
a = t.RawTurtle(win)
a.hideturtle()
a.pen(pencolor="yellow",pensize=10)




t.mainloop()



    
    