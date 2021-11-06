from copy import deepcopy
class stop:
    id = 0
    name = ""
    latitude = 0
    longitude = 0
    connections = []

    def __init__(self, id, name, longitude, latitude):
        self.id = id
        self.name = name
        self.latitude = latitude
        self.longitude = longitude
        self.connections = []

    def add_connection(self, stop, distance):
        self.connections.append((stop,distance))
    

    def __repr__(self):
        return self.name