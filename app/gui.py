import tkinter as tk
from tkinter.constants import *
import tkinter.font as tkFont
import backend as bk
import database as db
import paradas as pds
from PIL import Image,ImageTk

HEIGHT = 900
WIDTH = 900
path = []

main_window = tk.Tk()

main_window.title("Metro Kiev")
main_window.geometry(str(HEIGHT) + "x" + str(WIDTH))
main_window.config(bg='white')

frame = tk.Frame(main_window,width=WIDTH,height=125,bg="black")
frame.place(x=0,y=0)

fontStyle = tkFont.Font(family="Lucida Grande", size=12)
img = Image.open("./data/MetroKiev.png")
#img = tk.PhotoImage(file="./data/MetroKiev.png")
img = img.resize((500,500),Image.ANTIALIAS)
metro = ImageTk.PhotoImage(img)
label = tk.Label(main_window,image=metro)
label.place(x=120, y=150)

entry1 = tk.Entry(main_window)
entry1.place(x=WIDTH/32, y=HEIGHT/32)

entry2 = tk.Entry(main_window)
entry2.place(x=WIDTH/32, y=HEIGHT/32 + 50)

def update_text():
    path = bk.a_estrella(pds.buscar_parada(int(entry1.get())),pds.buscar_parada(int(entry2.get())))
    lbl = tk.Label(main_window,text=str(path),font=fontStyle,wraplength=800,justify=LEFT)
    lbl.place(x=WIDTH/32, y=HEIGHT-(HEIGHT/16))

button = tk.Button(main_window, text ="Buscar", command = update_text)
button.place(x=HEIGHT/32 + 200, y=HEIGHT/32 + 25)




while True:
    main_window.update_idletasks()
    main_window.update()
    
    
    