from f1 import *


fichero = "data/f1.csv"
ruta = lee_carreras(fichero)
# for e in ruta:
#     print(e)


#APARTADO 2    
res = media_tiempo_boxes(ruta, "Barcelona")
print(f"La media de tiempo en boxes en la ciudad de Barcelona es de {res} segundos")
print("------------------------------------------------------------------------------------")
#APARTADO 3
n=4
piloto_menos_tiempo = pilotos_menor_tiempo_medio_vueltas_top(ruta, n)
print(f"Los {n} pilotos con menor tiempo medio son {piloto_menos_tiempo}")
print("------------------------------------------------------------------------------------")

#APARTADO 4
ratio = ratio_tiempo_boxes_total(ruta)
for e in ratio:
    print(f"Los ratios del tiempo en boxes son: {e}")