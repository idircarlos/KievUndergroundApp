import math as m

class stop:
    id = 0
    name = ""
    latitude = 0
    longitude = 0
    connections = []
    coords = ()

    def __init__(self, id, name, longitude, latitude, coords=None):
        self.id = id
        self.name = name
        self.latitude = latitude
        self.longitude = longitude
        self.connections = []
        self.coords = coords

    def add_connection(self, stop, distance):
        self.connections.append((stop,distance))
    
    def __repr__(self):
        return self.name
    
    def is_in_circle (self, xp, yp):
        if self.coords == None:
            return False
        r = 15
        d = m.sqrt(pow(xp - self.coords[0],2) + pow((yp - self.coords[1]),2))
        if d <= r:
            return self
        else:
            return None
    
    
