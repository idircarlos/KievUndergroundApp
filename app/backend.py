from math import *
def distance_from_stops(start, finish):
    """Calulate the distance in km between two points on the earth (specified in decimal degrees)"""
    # convert decimal degrees to radians
    lon1, lat1, lon2, lat2 = map(radians, [start.lon, start.lat, finish.lon, finish.lat])

    # haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a))
    r = 6371 # Radius of earth in km
    
    # Return distance in km
    return c * r 

def a_star(start, end, trans):
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
        


print(distance_from_stops(40.594411, -3.981183, 40.595810, -3.985004))