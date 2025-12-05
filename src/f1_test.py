from f1 import *


def main():
    fichero = "data/f1.csv"
    ruta = lee_carreras(fichero)

    print("--------------------------------------------------")
    # APARTADO 2
    res = media_tiempo_boxes(ruta, "Abu Dhabi", None)
    print(f"La media de tiempo en boxes en la ciudad de Barcelona es de {res} segundos")
    print("--------------------------------------------------")

    # APARTADO 3
    n = 4
    piloto_menos_tiempo = pilotos_menor_tiempo_medio_vueltas_top(ruta, n)
    print(f"Los {n} pilotos con menor tiempo medio son {piloto_menos_tiempo}")
    print("--------------------------------------------------")

    # APARTADO 4
    ratio = ratio_tiempo_boxes_total(ruta)
    print("Test ratio_tiempo_boxes_total Los ratios del tiempo en boxes son:")
    for e in ratio:
        print(e)
    print("--------------------------------------------------")

    # APARTADO 5
    puntos = puntos_pilotos_anyos(ruta)
    print(puntos)
    print("--------------------------------------------------")

    # APARTADO 6
    anyo = 2023
    escuderia = mejor_escuderia_anyo(ruta, anyo)
    print(f"La mejor escudería en el año {anyo} ha sido {escuderia}.")
    print("--------------------------------------------------")


if __name__ == "__main__":
    main()


