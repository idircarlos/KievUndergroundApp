class stop:
    id = 0
    latitude = 0
    longitude = 0
    connections = []

    def __init__(self, id, latitude, longitude):
        self.id = id
        self.latitude = latitude
        self.longitude = longitude

    def add_connection(self, stop, distance):
        self.connections.append((stop,distance))
