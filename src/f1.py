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
            fecha_carrera = datetime.strptime(fecha_carrera, "%d-%m-%y")
            temperatura_min = int(temperatura_min)
            vel_max = float(vel_max)
            duracion = float(duracion)
            poisicion_final = int(poisicion_final)
            top_6_vueltas = parsea_vueltas(top_6_vueltas)
            tiempo_boxes = float(tiempo_boxes)
            nivel_liquido = bool(nivel_liquido)
            tupla = Carrera(nombre, escuderia, fecha_carrera, temperatura_min, vel_max, duracion, poisicion_final, ciudad, top_6_vueltas,tiempo_boxes,nivel_liquido)
            res.append(tupla)
    return res

def parsea_vueltas(lista_vueltas: str)->list[float]:
    lista = []
    lista_vueltas.replace("[", "") and lista_vueltas.replace("]", "")
    lista_vueltas.replace(" ","")
    for trozo in lista_vueltas.split("/"):
        if trozo == "-":
            lista.append(0.0)
        else:
            lista.append(float(trozo))
    return trozo
        


#Fernando Alonso;Aston Martin;21-11-22;25;330.1;30.5;-1;Abu Dhabi;[31.254/ 31.567/ 31.789/ 32.045/ -/ -];15.23;no