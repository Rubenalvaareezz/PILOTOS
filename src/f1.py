from collections import defaultdict
import csv
from datetime import date, datetime
from typing import NamedTuple

Carrera = NamedTuple("Carrera", 
            [("nombre", str),
             ("escuderia", str),
             ("fecha_carrera", date) ,
             ("temperatura_min", int),
             ("vel_max", float),
             ("duracion",float),
             ("posicion_final", int),
             ("ciudad", str),
             ("top_6_vueltas", list[float]),
             ("tiempo_boxes",float),
             ("nivel_liquido", bool)
            ])

def lee_carreras(fichero:str)-> list[Carrera]:
    with open(fichero, encoding= "utf-8") as f:
        lector = csv.reader(f, delimiter = ";")
        next(lector)
        res= []
        for nombre, escuderia, fecha_carrera, temperatura_min, vel_max, duracion, poisicion_final, ciudad, top_6_vueltas,tiempo_boxes,nivel_liquido in lector:
            fecha_carrera = datetime.strptime(fecha_carrera, "%d-%m-%y").date()
            temperatura_min = int(temperatura_min)
            vel_max = float(vel_max)
            duracion = float(duracion)
            poisicion_final = int(poisicion_final)
            top_6_vueltas = parsea_vueltas(top_6_vueltas)
            tiempo_boxes = float(tiempo_boxes)
            nivel_liquido = parsea_bool(nivel_liquido)
            tupla = Carrera(nombre, escuderia, fecha_carrera, temperatura_min, vel_max, duracion, poisicion_final, ciudad, top_6_vueltas,tiempo_boxes,nivel_liquido)
            res.append(tupla)
    return res

def parsea_vueltas(lista_vueltas: str)->list[float]:
    lista_vueltas = lista_vueltas.replace("[", "").replace("]", "").replace(" ","")
    lista = []
    for trozo in lista_vueltas.split("/"):
        if trozo == "-":
            lista.append(0.0)
        else:
            lista.append(float(trozo))
    return lista
def parsea_bool(nivel_liquido:str)->bool:
    valor = nivel_liquido.strip().lower()
    return valor in ("1","sí","true")

def media_tiempo_boxes(carreras:list[Carrera], ciudad:str, fecha:date | None =None)->float:
    fechas = None
    lista = []
    for e in carreras:
        if (fechas == None or fechas == fecha) and e.ciudad == ciudad:
            lista.append(e.tiempo_boxes)
            media = sum(lista)/len(lista)
            
        elif fecha == None:
            if ciudad == e.ciudad:
                lista.append(e.tiempo_boxes)
                media = sum(lista)
           
        else: 
            media = 0.0
    return media

            
def pilotos_menor_tiempo_medio_vueltas_top(carreras:list[Carrera], n)->list[tuple[str,date]]:
    lista = []
    for e in carreras:
        if 0 not in e.top_6_vueltas:
            media_top = sum(e.top_6_vueltas) / len(e.top_6_vueltas)
            lista.append((media_top, e.nombre, e.fecha_carrera))
           
    lista.sort()
    return [(e[1],e[-1]) for e in lista][:n]


def ratio_tiempo_boxes_total(carreras:list[Carrera])->list[tuple[str,date, float]]:
    tiempo_total = defaultdict(float)
    for e in carreras:
        tiempo_total[e.fecha_carrera] += e.tiempo_boxes
    lista = [(e.nombre,e.fecha_carrera,(e.tiempo_boxes/tiempo_total[e.fecha_carrera])) for e in carreras]
        
    return  sorted(lista, key= lambda t:t[2], reverse=True)
        



