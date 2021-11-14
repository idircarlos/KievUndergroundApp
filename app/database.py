from stop import *

#LINEA 1
stop_110 = stop(110, "Akademmistechko", 50.465015978082526, 30.355187524584036,(-85, 53))
stop_111 = stop(111, "Zhytomyrska", 50.4562624472573, 30.365438029230255,(-85, 23))
stop_112 = stop(112, "Sviatoshyn", 50.45776584808692, 30.39065662860456,(-85, -7))
stop_113 = stop(113, "Nyvky", 50.458646796231385, 30.404370570917912,(-52, -51))
stop_114 = stop(114, "Beresteiska", 50.459319913935715, 30.418634956425073,(-29, -51))
stop_115 = stop(115, "Shuliavska", 50.45422886457714, 30.448621031538917,(5, -51))
stop_116 = stop(116, "Politekhnichnyi instytut", 50.45112975151065, 30.464291731567478,(38, -51))
stop_117 = stop(117, "Vokzalna", 50.441333629319324, 30.489964536301958,(73, -51))
stop_118 = stop(118, "Universytet", 50.44326693084893, 30.504630159030405,(106, -51))
stop_119 = stop(119, "Teatralna", 50.4447938150602, 30.515523470292727,(162, 22))
stop_120 = stop(120, "Khreshchatyk", 50.44734547179228, 30.522758804051335,(230, 22))
stop_121 = stop(121, "Arsenalna", 50.44306249715046, 30.547156635699498,(309, 22))
stop_122 = stop(122, "Dnipro", 50.44122885349573, 30.559336714113712,(365.0, 22.0))
stop_123 = stop(123, "Hidropark", 50.44597803424576, 30.57688217382897,(421.0, 22.0))
stop_124 = stop(124, "Livoberezhna", 50.45186552590256, 30.598156861534004,(443.0, 52.0))
stop_125 = stop(125, "Darnytsia", 50.45595887549448, 30.612968983504803,(465.0, 81.0))
stop_126 = stop(126, "Chernihivska", 50.45989135620235, 30.63029161718559,(488.0, 111.0))
stop_127 = stop(127, "Lisova", 50.46465878887907, 30.645564379174083,(511.0, 140.0))

stop_110.add_connection(stop_111, 1.4)

stop_111.add_connection(stop_110, 1.4)
stop_111.add_connection(stop_112, 1.9)

stop_112.add_connection(stop_111, 1.9)
stop_112.add_connection(stop_113, 1.1)

stop_113.add_connection(stop_112, 1.1)
stop_113.add_connection(stop_114, 1.1)

stop_114.add_connection(stop_113, 1.1)
stop_114.add_connection(stop_115, 2.1)

stop_115.add_connection(stop_114, 2.1)
stop_115.add_connection(stop_116, 1.3)

stop_116.add_connection(stop_115, 1.3)
stop_116.add_connection(stop_117, 1.9)

stop_117.add_connection(stop_116, 1.9)
stop_117.add_connection(stop_118, 1.3)

stop_118.add_connection(stop_117, 1.3)
stop_118.add_connection(stop_119, 0.7)

stop_119.add_connection(stop_118, 0.7)
stop_119.add_connection(stop_120, 0.68)

stop_120.add_connection(stop_119, 0.68)
stop_120.add_connection(stop_121, 1.6)

stop_121.add_connection(stop_120, 1.6)
stop_121.add_connection(stop_122, 0.98)

stop_122.add_connection(stop_121, 0.98)
stop_122.add_connection(stop_123, 1.4)

stop_123.add_connection(stop_122, 1.4)
stop_123.add_connection(stop_124, 1.6)

stop_124.add_connection(stop_123, 1.6)
stop_124.add_connection(stop_125, 1.2)

stop_125.add_connection(stop_124, 1.2)
stop_125.add_connection(stop_126, 1.4)

stop_126.add_connection(stop_125, 1.4)
stop_126.add_connection(stop_127, 1.3)

stop_127.add_connection(stop_126, 1.3)



#LINEA 2
stop_210 = stop(210, "Heroiv Dnipra", 50.522740115696095, 30.498865386439537, (230, 288))
stop_211 = stop(211, "Misnka", 50.512393659306554, 30.498569221632515, (230, 258))
stop_212 = stop(212, "Obolon", 50.501581630277876, 30.498181213966017, (230, 228))
stop_213 = stop(213, "Petrivka", 50.486128624743856, 30.497810402147852, (230, 185))
stop_214 = stop(214, "Tarasa Shevchenka", 50.47405371124174, 30.503810286293774, (230, 156))
stop_215 = stop(215, "Kontraktova ploshcha", 50.46607925893003, 30.514818775653413, (230, 126))
stop_216 = stop(216, "Poshtova Ploshcha", 50.45935094255671, 30.524454912880408, (230, 96))
stop_217 = stop(217, "Maidan Nezalezhnosti", 50.448170402557466, 30.524998433103274, (230, 52))
stop_218 = stop(218, "Ploshcha Lva Tolstogo", 50.44028544161946, 30.518358539865226, (230, -35))
stop_219 = stop(219, "Olimpiiska", 50.43138495960601, 30.516836511029062, (230, -110))
stop_220 = stop(220, "Palats Ukrania", 50.42149290924991, 30.520717864999927, (230, -140))
stop_221 = stop(221, "Lybidska", 50.414611259014, 30.524961651353486, (230, -168))
stop_222 = stop(222, "Demiivska", 50.404803456026684, 30.516850277809592, (230, -198))
stop_223 = stop(223, "Holosiivska", 50.39742117717732, 30.50825907270707, (185, -256))
stop_224 = stop(224, "Vasylkivska", 50.39342415294817, 30.488205370300193, (152, -256))
stop_225 = stop(225, "Vystavkovyi tsentr", 50.38247519076805, 30.477554159536847, (130, -256))
stop_226 = stop(226, "Ipodrom", 50.37661806622592, 30.468823310597116, (106, -256))
stop_227 = stop(227, "Teremky", 50.36709545601481, 30.45415814797518, (84, -256))

stop_210.add_connection(stop_211, 1.2)

stop_211.add_connection(stop_210, 1.2)
stop_211.add_connection(stop_212, 1.2)

stop_212.add_connection(stop_211, 1.2)
stop_212.add_connection(stop_213, 1.7)

stop_213.add_connection(stop_212, 1.7)
stop_213.add_connection(stop_214, 1.4)

stop_214.add_connection(stop_213, 1.4)
stop_214.add_connection(stop_215, 1.2)

stop_215.add_connection(stop_214, 1.2)
stop_215.add_connection(stop_216, 1.0)

stop_216.add_connection(stop_215, 1.0)
stop_216.add_connection(stop_217, 1.3)

stop_217.add_connection(stop_216, 1.3)
stop_217.add_connection(stop_218, 0.988)


stop_218.add_connection(stop_217, 0.988)
stop_218.add_connection(stop_219, 1.1)


stop_219.add_connection(stop_218, 1.1)
stop_219.add_connection(stop_220, 1.2)

stop_220.add_connection(stop_219, 1.2)
stop_220.add_connection(stop_221, 0.836)

stop_221.add_connection(stop_220, 0.836)
stop_221.add_connection(stop_222, 1.2)

stop_222.add_connection(stop_221, 1.2)
stop_222.add_connection(stop_223, 1.1)

stop_223.add_connection(stop_222, 1.1)
stop_223.add_connection(stop_224, 2.9)

stop_224.add_connection(stop_223, 2.9)
stop_224.add_connection(stop_225, 1.5)

stop_225.add_connection(stop_224, 1.5)
stop_225.add_connection(stop_226, 0.924)

stop_226.add_connection(stop_225, 0.924)
stop_226.add_connection(stop_227, 1.48)

stop_227.add_connection(stop_226, 1.48)


#LINEA 3
stop_310 = stop(310, "Syrets", 50.47681524614531, 30.432776504083396, (50,110))
stop_311 = stop(311, "Dorohozhychi", 50.473475677999296, 30.449127599772154, (72, 81))
stop_312 = stop(312, "Lukianivska", 50.46119338085303, 30.48362944618976, (95, 51))
stop_314 = stop(314, "Zoloti Vorota", 50.448711867661686, 30.514327876851468, (117, 23))
stop_315 = stop(315, "Palats Sportu", 50.43979614334605, 30.519507456240333, (230, -66))
stop_316 = stop(316, "Klovska", 50.4370916819905, 30.531860642749198, (286, -66))
stop_317 = stop(317, "Pecherska", 50.427383037449836, 30.539397998567257, (309, -95))
stop_318 = stop(318, "Druzhby Narodiv", 50.41713552475245, 30.54728481205805, (331, -125))
stop_319 = stop(319, "Vydubychi", 50.40195875036084, 30.56047726973022, (354, -154))
stop_321 = stop(321, "Slavutych", 50.39431612062926, 30.604837229481692, (376, -183))
stop_322 = stop(322, "Osokorky", 50.39532261410228, 30.616203209987702, (398, -212))
stop_323 = stop(323, "Pozniaky", 50.39788991357751, 30.634739567651373, (421, -242))
stop_324 = stop(324, "Kharkivska", 50.400847047155395, 30.65205731205759, (455.0, -286.0))
stop_325 = stop(325, "Vyrlytsia", 50.402951109703366, 30.66691051948101,(477.0, -287.0))
stop_326 = stop(326, "Boryspilska", 50.403465565753365, 30.684370370647205,(499.0, -286.0))
stop_327 = stop(327, "Chervonyi khutir", 50.40954636743697, 30.69623245641607,(523.0, -286.0))

stop_310.add_connection(stop_311 ,1.5)

stop_311.add_connection(stop_310 ,1.5)
stop_311.add_connection(stop_312 ,2.7)

stop_312.add_connection(stop_311 ,2.7)
stop_312.add_connection(stop_314 ,3.1)

stop_314.add_connection(stop_312 ,3.1)
stop_314.add_connection(stop_315 ,0.757)

stop_315.add_connection(stop_314, 0.757)
stop_315.add_connection(stop_316, 1.1)

stop_316.add_connection(stop_315, 1.1)
stop_316.add_connection(stop_317, 1.3)

stop_317.add_connection(stop_316, 1.3)
stop_317.add_connection(stop_318, 1.1)

stop_318.add_connection(stop_317, 1.1)
stop_318.add_connection(stop_319, 1.9)

stop_319.add_connection(stop_318, 1.9)
stop_319.add_connection(stop_321, 3.4)

stop_321.add_connection(stop_319, 3.4)
stop_321.add_connection(stop_322, 0.795)

stop_322.add_connection(stop_321, 0.795)
stop_322.add_connection(stop_323, 1.4)

stop_323.add_connection(stop_322, 1.4)
stop_323.add_connection(stop_324, 1.3)

stop_324.add_connection(stop_323, 1.3)
stop_324.add_connection(stop_325, 1.1)

stop_325.add_connection(stop_324, 1.1)
stop_325.add_connection(stop_326, 1.2)

stop_326.add_connection(stop_325, 1.2)
stop_326.add_connection(stop_327, 2.3)

stop_327.add_connection(stop_326, 2.3)

#Transbordos linea 1
stop_119.add_connection(stop_314, 0.601)
stop_120.add_connection(stop_217, 0.601)

#Transbordos linea 2
stop_217.add_connection(stop_120, 0.601)
stop_218.add_connection(stop_315, 1.2)

#Transbordos linea 3
stop_314.add_connection(stop_119, 0.601)
stop_315.add_connection(stop_218, 1.2)


""" METODOS DE LA CLASE """
import paradas

#Encontrar la parada dadas unas coordenadas
def which_stop(x,y):
    for parada in paradas.lista_paradas:
        ret = parada.is_in_circle(x,y)
        if ret is None or False:
            continue
        elif ret is parada:
            return ret
