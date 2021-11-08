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



HEIGHT = 1000
WIDTH = 1000
path = []

main_window = tk.Tk()

main_window.title("Metro Kiev")
main_window.geometry(str(HEIGHT) + "x" + str(WIDTH))
main_window.config(bg='white')

""" Barra negra de arriba
frame = tk.Frame(main_window,width=WIDTH,height=125,bg="black")
frame.place(x=0,y=0)
"""

""" Fuente del texto de la ruta """
fontStyle = tkFont.Font(family="Lucida Grande", size=12)

""" Imagen del metro """
img = Image.open("./app/MetroKiev.png")
#img = tk.PhotoImage(file="./data/MetroKiev.png")
img = img.resize((800,800),Image.ANTIALIAS)
metro = ImageTk.PhotoImage(img)
label = tk.Label(main_window,image=metro)
label.place(x=70, y=90)

""" Caja de texto 1
entry1 = tk.Entry(main_window)
entry1.place(x=WIDTH/32, y=HEIGHT/32)
""" 
"""Caja de texto 2
entry2 = tk.Entry(main_window)
entry2.place(x=WIDTH/32, y=HEIGHT/32 + 50)
"""
inicio = None
destino = None
pulsado = False

def printcoords(event):
    #outputting x and y coords to console
    global inicio, destino, pulsado
    #print (event.x,event.y)
    #mouseclick event
    if pulsado == False:
        inicio = db.which_stop(event.x, event.y)
        print("Inicio: " + str(inicio))
        pulsado = True
    else:
        destino = db.which_stop(event.x, event.y)
        print("Destino: " + str(destino))
        print()
        return bk.a_estrella(inicio,destino)
    
main_window.bind("<Button 1>",printcoords)

def update_text():
    path = bk.a_estrella(pds.buscar_parada(int(entry1.get())),pds.buscar_parada(int(entry2.get())))
    lbl = tk.Label(main_window,text=str(path),font=fontStyle,wraplength=800,justify=LEFT)
    lbl.place(x=WIDTH/32, y=HEIGHT-(HEIGHT/16))

#button = tk.Button(main_window, text ="", command = update_text, borderwidth=0,image=tk.PhotoImage(file="./app/boton.png"))
#button.place(x=185, y=210)

"""
circulo = Image.new("RGBA", (200, 200), (255,0,0,0))
draw = ImageDraw.Draw(circulo)
 #Draw a rounded rectangle
draw.rounded_rectangle((0, 0, 200, 200), fill="white", outline="black",width=45, radius=100)
circulo.save("app/circulo_parada100.png")


btn = rd.RoundedButton(main_window,radius=100, btnbackground="#0078ff", btnforeground="#ffffff")
btn.place(x=140,y=240)


imageres = Image.open("app/circulo_parada100.png")
imageres = imageres.resize((15,15),Image.ANTIALIAS)
imagetest = ImageTk.PhotoImage(imageres)
button2 = tk.Button(main_window,border=0, height=15, width=15)
button2.config(image=imagetest)
button2.place(x=185,y=210)
"""
"""
button = tk.Button()
button_load = Image.open('app/circulo_parada100.gif')
button_image = ImageTk.PhotoImage(button_load)
button.config(image=button_image,border=0)
button.place(x=200,y=200)
"""




""" Boton de buscar
button = tk.Button(main_window, text ="Buscar", command = update_text)
button.place(x=HEIGHT/32 + 200, y=HEIGHT/32 + 25)
"""



while True:
    main_window.update_idletasks()
    main_window.update()
    
    
    