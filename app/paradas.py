import database as db

lista_paradas = []

# Linea 1
lista_paradas.append(db.stop_110)
lista_paradas.append(db.stop_111)
lista_paradas.append(db.stop_112)
lista_paradas.append(db.stop_113)
lista_paradas.append(db.stop_114)
lista_paradas.append(db.stop_115)
lista_paradas.append(db.stop_116)
lista_paradas.append(db.stop_117)
lista_paradas.append(db.stop_118)
lista_paradas.append(db.stop_119)
lista_paradas.append(db.stop_120)
lista_paradas.append(db.stop_121)
lista_paradas.append(db.stop_122)
lista_paradas.append(db.stop_123)
lista_paradas.append(db.stop_124)
lista_paradas.append(db.stop_125)
lista_paradas.append(db.stop_126)
lista_paradas.append(db.stop_127)

# Linea 2
lista_paradas.append(db.stop_210)
lista_paradas.append(db.stop_211)
lista_paradas.append(db.stop_212)
lista_paradas.append(db.stop_213)
lista_paradas.append(db.stop_214)
lista_paradas.append(db.stop_215)
lista_paradas.append(db.stop_216)
lista_paradas.append(db.stop_217)
lista_paradas.append(db.stop_218)
lista_paradas.append(db.stop_219)
lista_paradas.append(db.stop_220)
lista_paradas.append(db.stop_221)
lista_paradas.append(db.stop_222)
lista_paradas.append(db.stop_223)
lista_paradas.append(db.stop_224)
lista_paradas.append(db.stop_225)
lista_paradas.append(db.stop_226)
lista_paradas.append(db.stop_227)


# Linea 3
lista_paradas.append(db.stop_310)
lista_paradas.append(db.stop_311)
lista_paradas.append(db.stop_312)
lista_paradas.append(db.stop_314)
lista_paradas.append(db.stop_315)
lista_paradas.append(db.stop_316)
lista_paradas.append(db.stop_317)
lista_paradas.append(db.stop_318)
lista_paradas.append(db.stop_319)
lista_paradas.append(db.stop_321)
lista_paradas.append(db.stop_322)
lista_paradas.append(db.stop_323)
lista_paradas.append(db.stop_324)
lista_paradas.append(db.stop_325)
lista_paradas.append(db.stop_326)
lista_paradas.append(db.stop_327)

def buscar_parada(id):
    for parada in lista_paradas:
        if parada.id == id:
            return parada
    return "No encontrado"