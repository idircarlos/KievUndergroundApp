from tkinter.constants import *
import backend as bk
import database as db
import turtle as t

HEIGHT = 1000
WIDTH = 1000

""" Resizer Imagen del metro """
#img = Image.open("./app/img/metrobien.png")
#img = img.resize((900,900),Image.ANTIALIAS)
#img.save("./app/img/metrobienresized.png")

""" Variables globales """
inicio = None
destino = None
buscaSegundaParada = False

# Dibujar camino dada una lista
def draw_path(path):
    if path == None:
        print("Can't draw an empty path")
        return
    a.penup()
    a.speed(0)
    a.goto((path[0].coords[0], path[0].coords[1]))
    a.speed(2.5)
    
    for parada in path:
        a.color('yellow')
        a.pendown()
        a.goto(parada.coords[0],parada.coords[1])
        a.penup()
        
    a.goto(path[0].coords[0], path[0].coords[0])
    a.showturtle()
    for parada in path:
        a.color('black') 
        a.pendown()
        if parada is not path[-1]:
            a.dot(15)
        a.penup()
        a.goto(parada.coords[0],parada.coords[1])

# Llama a A* con las dos paradas
def printcoords(x,y):
    global inicio, destino, buscaSegundaParada, a
    # Muestra las coordenadas del click por consola
    print (x,y)
    
    # Primera parada
    if buscaSegundaParada == False:
        inicio = db.which_stop(x, y)
        if inicio is None:
            return
        # Muestra el inicio por consola
        print("Inicio: " + str(inicio))
        buscaSegundaParada = True
    # Segunda parada
    else:
        destino = db.which_stop(x, y)
        if destino is None:
            return
        # Muestra el destino por consola y reinicia el buscador
        print("Destino: " + str(destino))
        print()
        buscaSegundaParada = False
        # Dibuja el camino
        path = bk.a_estrella(inicio,destino)
        draw_path(path) 
 
    
""" Ventanta principal """
win = t.Screen()
# Background
win.bgpic("./app/img/metrobienresized.png")
win.setup(height=HEIGHT, width=WIDTH)
win.title("Metro Kiev")
win.register_shape("./app/img/icono_metro.gif")
#Selecciona a una parada
win.onclick(printcoords,1)

#Pintar camino
a = t.RawTurtle(win)
a.hideturtle()
a.pen(pensize=10)
a.color('yellow')
a.shape("./app/img/icono_metro.gif")
# Llama en un bucle al programa
t.mainloop()
