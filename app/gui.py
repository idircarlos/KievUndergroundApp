from tkinter.constants import *
import backend as bk
import database as db
import turtle as t

HEIGHT = 900
WIDTH = 1267

""" Resizer Imagen del metro """
#img = Image.open("./app/img/metrobien.png")
#img = img.resize((900,900),Image.ANTIALIAS)
#img.save("./app/img/metrobienresized.png")

""" Variables globales """
inicio = None
destino = None
buscaSegundaParada = False
otroViaje = False
dibujando = False
color_line = '#d1b04b'
# Dibujar camino dada una lista
def draw_path(path):
    global otroViaje
    index = 0
    a.color(color_line)
    if path == None:
        print("Can't draw an empty path")
        return
    a.penup()
    a.speed(0)
    a.goto((path[0].coords[0], path[0].coords[1]))
    a.speed(2.5)
    while index < len(path):
        parada = path[index]
        a.pendown()
        a.goto(parada.coords[0],parada.coords[1])
        if index+1 < len(path) and ((parada.id == 314 and path[index+1].id == 315) or (parada.id == 315 and path[index+1].id == 314)):
            a.goto(162,22)
        a.penup()
        index = index + 1
    a.speed(0)
    a.goto(path[0].coords[0],path[0].coords[1])
    a.speed(2.5)
    a.color('black')
    index = 0
    for parada in path:
        a.goto(parada.coords[0], parada.coords[1])
        a.showturtle()
        if parada is not path[-1]:
            a.dot(15)
        if index+1 < len(path) and ((parada.id == 314 and path[index+1].id == 315) or (parada.id == 315 and path[index+1].id == 314)):
            a.goto(162,22)
        index = index + 1
    a.color(color_line)
    a.hideturtle()
    a.stamp()
    a.penup()
    win.bgpic("./app/img/metrobienresized3.png")
    otroViaje = True
      
# Comprueba si se ha clickado la flecha    
def in_flecha(x,y):
    if x > -603 and x < -523 and y > -410 and y < -382:
        return True 
    return False       
# Comprueba si se ha clickado el reset
def in_reset(x,y):
    if x > -484 and x < -268 and y > -425 and y < -365:
        return True 
    return False

# Dibuja el id de la parada
def dibujar_parada(parada, id):
    a.speed(0)
    s = str(id)
    color_boli(id)
    a.penup()
    if parada == 1:
        a.goto((-400.0, 209.5))
    elif parada == 2:
        a.goto((-400.0, -2))
    a.pendown()
    a.write(s,align=CENTER, font=('Arial', 14, 'normal'))
    a.penup()

def color_boli(id):
    if id > 300:
        a.color('green')
    elif id > 200:
        a.color('blue')
    elif id > 100:
        a.color('red')
    
# Llama a A* con las dos paradas
def printcoords(x,y):
    global inicio, destino, buscaSegundaParada, otroViaje, dibujando, a
    # Muestra las coordenadas del click por consola
    print (x,y)
    
    # Primera parada
    if buscaSegundaParada == False:
        inicio = db.which_stop(x, y)
        if inicio is None:
            return
        a.penup()
        a.goto(inicio.coords[0], inicio.coords[1])
        a.color('#8c8a89')
        a.penup()
        a.dot(15)
        # Muestra el inicio por consola
        print("Inicio: " + str(inicio))
        buscaSegundaParada = True
        win.bgpic("./app/img/metrobienresized2.png")
        dibujar_parada(1, inicio.id)
        
    # Segunda parada
    else:
        if otroViaje == True: 
            dibujando = False
            if in_flecha(x,y):
                a.clear()
                dibujar_parada(1,inicio.id)
                a.penup()
                a.goto(inicio.coords[0], inicio.coords[1])
                a.color('#8c8a89')
                a.penup()
                a.dot(15)
                
                otroViaje = False
                win.bgpic("./app/img/metrobienresized2.png")     
            if in_reset(x,y):
                a.clear()
                buscaSegundaParada = False
                otroViaje = False
                win.bgpic("./app/img/metrobienresized1.png")
            return
        
        elif not dibujando and in_flecha(x,y):
            a.clear()
            buscaSegundaParada = False
            win.bgpic("./app/img/metrobienresized1.png")
            return
        
        destino = db.which_stop(x, y)
        if destino is None:
            return
        # Muestra el destino por consola y reinicia el buscador
        print("Destino: " + str(destino))
        print()
        # Dibuja el camino
        path = bk.a_estrella(inicio,destino)
        win.bgpic("./app/img/metrobienresized2-5.png")
        dibujar_parada(2,destino.id)
        dibujando = True
        draw_path(path)
 
    
""" Ventanta principal """
win = t.Screen()
win.setup(width=WIDTH, height=HEIGHT, startx=None, starty=None)
# Background
win.bgpic("./app/img/metrobienresized1.png")
win.setup(height=HEIGHT, width=WIDTH)
win.title("Metro Kiev")
win.register_shape("./app/img/icono_metro.gif")
#Selecciona a una parada
win.onclick(printcoords,1)

#Pintar camino
a = t.RawTurtle(win)
a.speed(0)
a.hideturtle()
a.pen(pensize=6)
a.color('purple')
a.shape("./app/img/icono_metro.gif")
a.penup()
# Llama en un bucle al programa
t.mainloop()
