import backend as bk
from stop import *

a = stop(1,3,4)
b = stop(4,3,4)

prueba = bk.var

c = bk.distance_from_stops(a,b)
print(c)