from math import *
import database as db

# Calcula la distancia entre dos puntos de la tierra en km, se usa para obtener h()
def distancia_entre_dos_paradas(inicio, fin):
    # Convierte de decimales a radianes
    lon1, lat1, lon2, lat2 = map(radians, [inicio.longitude, inicio.latitude, fin.longitude, fin.latitude])

    # Formula haversine
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a))
    r = 6371 # Radio de la tierra en km
    
    return c * r # Distancia en km

# Algoritmo A*, basado en la implemtacion de f() = g() + h()
def a_estrella(inicio, fin):
    # Lista de paradas que han sido estudiadas pero sus vecinos aun no
    lista_abierta = set([inicio])
    # Lista de paradas que ya han sido estudiadas incluyendo sus vecinos
    lista_cerrada = set([])

    # Contiene las distancias actuales del comienzo al resto de nodos f(), su valor por defecto es +infinito
    distancias_f = {}
    distancias_f[inicio] = 0

    # Contiene un mapeado de todas las paradas adyacentes
    adyacentes = {}
    adyacentes[inicio] = inicio

    while fin not in lista_cerrada:
        estudiando = None
        # Busca un nodo con el menor valor f()
        for v in lista_abierta:
            if estudiando == None or distancias_f[v] + distancia_entre_dos_paradas(v, fin) < distancias_f[estudiando] + distancia_entre_dos_paradas(estudiando, fin):
                estudiando = v

        if estudiando == None:
            print('No existe el camino')
            return None

        # Si el nodo estudiando es el final empezamos otra vez desde el inicio
        if estudiando == fin:
            reconstruir_camino = []

            while adyacentes[estudiando] != estudiando:
                reconstruir_camino.append(estudiando)
                estudiando = adyacentes[estudiando]

            reconstruir_camino.append(inicio)
            reconstruir_camino.reverse()

            print('Camino encontrado: {}'.format(reconstruir_camino))
            return reconstruir_camino

        # Para todos los vecinos miramos:
        for (vecino, peso_g) in estudiando.connections:
            # Si el nodo no esta ni en la lista cerrada ni en la abierta
            # se le anade a la lista abierta y se guarda como adyacente
            if vecino not in lista_abierta and vecino not in lista_cerrada:
                lista_abierta.add(vecino)
                adyacentes[vecino] = estudiando
                distancias_f[vecino] = distancias_f[estudiando] + peso_g

            # Sino, miramos si es mas rapido visitar el vecino 
            # Si lo es actualiza distnacia_f y adyacentes
            else:
                if distancias_f[vecino] > distancias_f[estudiando] + peso_g:
                    distancias_f[vecino] = distancias_f[estudiando] + peso_g
                    adyacentes[vecino] = estudiando
                    # Si el nodo estaba en la lista cerrada lo movemos a la lista abierta
                    if vecino in lista_cerrada:
                        lista_cerrada.remove(vecino)
                        lista_abierta.add(vecino)

        # Borra el nodo estudiando de la lista abierta y lo anade
        #  a la cerrada porque ya hemos analizado todos sus vecinos
        lista_abierta.remove(estudiando)
        lista_cerrada.add(estudiando)

    print('No existe el camino')
    return None