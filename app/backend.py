from math import *
import database as db

def distance_from_stops(start, finish):
    """Calulate the distance in km between two points on the earth (specified in decimal degrees)"""
    # convert decimal degrees to radians
    lon1, lat1, lon2, lat2 = map(radians, [start.longitude, start.latitude, finish.longitude, finish.latitude])

    # haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a))
    r = 6371 # Radius of earth in km
    
    # Return distance in km
    return c * r 

def a_star(start, end):
    initial_distance = distance_from_stops(start,end) if start != end else 0
    open_list = {start: {"g": 0, "h": initial_distance, "f": initial_distance, "father": -1}}
    close_list = {} #{idNodo : idNodoPadre}
    final_weight = 0

    # f(n) = g(n) + h(n)
    while(end not in close_list.keys()):
        this_node_id = sorted(open_list, key=lambda elem: open_list[elem]["f"])[0]
        this_node = open_list[this_node_id].copy()

        if(this_node == end):
            final_weight = this_node["f"]

        close_list[this_node_id] = this_node["father"]
        del open_list[this_node_id]
        if(len(this_node.conn) == 0):
            continue

        ####################################################################

def a_star_algorithm(start, end):
    # In this open_lst is a list of nodes which have been visited, but who's 
    # neighbours haven't all been always inspected, It starts off with the start node
    # And closed_list is a list of nodes which have been visited
    # and who's neighbors have been always inspected
    open_lst = set([start])
    closed_lst = set([])

    # poo has present distances from start to all other nodes
    # the default value is +infinity
    distances = {}
    distances[start] = 0

    # par contains an adjac mapping of all nodes
    adjacents = {}
    adjacents[start] = start

    i=1
    while end not in closed_lst:
        estudiando = None
        print("iteracion: " +str(i))
        # it will find a node with the lowest value of f() -
        for v in open_lst:
            if estudiando == None or distances[v] + distance_from_stops(v, end) < distances[estudiando] + distance_from_stops(estudiando, end):
                #print(v)
                #print(distance_from_stops(v, end))
                #print(distance_from_stops(db.stop_111, end))
                estudiando = v

        if estudiando == None:
            print('Path does not exist!')
            return None

        # if the current node is the stop
        # then we start again from start
        if estudiando == end:
            reconst_path = []

            while adjacents[estudiando] != estudiando:
                reconst_path.append(estudiando)
                estudiando = adjacents[estudiando]

            reconst_path.append(start)

            reconst_path.reverse()

            print('Path found: {}'.format(reconst_path))
            return reconst_path

        # for all the neighbors of the current node do
        print(estudiando)
        print(estudiando.connections)
        for (m, weight) in estudiando.connections:
            print("Entra for con: "+ str(m))
            # if the current node is not presentin both open_lst and closed_lst
            # add it to open_lst and note n as it's par
            if m not in open_lst and m not in closed_lst:
                print("Entra if con: " +str(m))
                open_lst.add(m)
                adjacents[m] = estudiando
                distances[m] = distances[estudiando] + weight

            # otherwise, check if it's quicker to first visit n, then m
            # and if it is, update par data and poo data
            # and if the node was in the closed_lst, move it to open_lst
            else:
                print("Entra else con: " + str(m))
                if distances[m] > distances[estudiando] + weight:
                    distances[m] = distances[estudiando] + weight
                    adjacents[m] = estudiando

                    if m in closed_lst:
                        closed_lst.remove(m)
                        open_lst.add(m)

        # remove n from the open_lst, and add it to closed_lst
        # because all of his neighbors were inspected
        open_lst.remove(estudiando)
        closed_lst.add(estudiando)
        print()
        i = i + 1

    print('Path does not exist!')
    return None