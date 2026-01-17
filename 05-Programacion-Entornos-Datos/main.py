#! /usr/bin/python3

import argparse
import os
from itertools import groupby

import practica

years = range(2001,2025)
users = range(0,150)


def ordenaDict(d):
    return dict(sorted(d.items()))

def ordenaListaPorBloques(lst):
    res = []
    for clave, grupo in groupby(lst, key=lambda x: x[1]):
        bloque = list(grupo)
        bloque.sort(key=lambda x: x[0])
        res.extend(bloque)
    return res


def main():
    parser = argparse.ArgumentParser(description='Práctica PED 2025/2026')
    parser.add_argument('--path', default=".", type=str, help='Ruta de la carpeta donde se encuentran los .csv')
    
    args = parser.parse_args()

    # Primero creamos la lista de rutas.
    paths_csv = []
    for ifile in os.listdir(args.path):
        if ifile.endswith(".csv"):
            fullpath = os.path.join(args.path, ifile)
            paths_csv.append(fullpath)

    # EJERCICIO 2
    df = practica.loadData(paths_csv)

    # EJERCICIO 3
    print ("Ejercicio 3")
    print ("a) Libro más prestado en global:", end=" ")
    print (practica.bestBook(df))
    for y in years:
        print ("   Libro más prestado en el año",str(y)+":", end=" ")
        print (practica.bestBookYear(df,y))
    print ("b) Género más prestado en global:", end=" ")
    print (practica.bestGenre(df))
    for y in years:
        print ("   Género más prestado en el año",str(y)+":", end=" ")
        print (practica.bestGenreYear(df,y))
    print ("c) Lector con más préstamos en global:", end=" ")
    print (practica.bestReader(df))
    for y in years:
        print ("   Lector con más préstamos en el año",str(y)+":", end=" ")
        print (practica.bestReaderYear(df,y))
    print ("d) Lector con más días acumulados de préstamo en global:", end=" ")
    print (practica.mostAccumulatedDays(df))
    for y in years:
        print ("   Lector con más días acumulados de préstamo en el año",str(y)+":", end=" ")
        print (practica.mostAccumulatedDaysYear(df,y))
    print ("e) Información sobre cada usuario")
    for u in users:
        uid = "lector"+('00'+str(u))[-3:]
        print ("   Datos del lector",uid,"en global:", end=" ")
        res = practica.userInfo(df,uid)
        res["Géneros"] = ordenaDict(res["Géneros"])
        print (ordenaDict(res))
        for y in years:
            print ("   Datos del lector",uid,"en el año",str(y)+":", end=" ")
            res = practica.userInfoYear(df,uid,y)
            res["Géneros"] = ordenaDict(res["Géneros"])
            print (ordenaDict(res))

    # EJERCICIO 4
    print ("Ejercicio 4")
    print ("a) Libro más renovado en global:", end=" ")
    print (practica.mostRenewedBook(df))
    for y in years:
        print ("   Libro más renovado en el año",str(y)+":", end=" ")
        print (practica.mostRenewedBookYear(df,y))
    print ("b) Libro más rápido en ser leído en global:", end=" ")
    print (practica.fastestBook(df))
    for y in years:
        print ("   Libro más rápido en ser leído en el año",str(y)+":", end=" ")
        print (practica.fastestBookYear(df,y))
    print ("c) Libro más lento en ser leído en global:", end=" ")
    print (practica.slowestBook(df))
    for y in years:
        print ("   Libro más lento en ser leído en el año",str(y)+":", end=" ")
        print (practica.slowestBookYear(df,y))
    print ("d) Género más rápido en ser leído en global:", end=" ")
    print (practica.fastestGenre(df))
    for y in years:
        print ("   Género más rápido en ser leído en el año",str(y)+":", end=" ")
        print (practica.fastestGenreYear(df,y))
    print ("e) Género más lento en ser leído en global:", end=" ")
    print (practica.slowestGenre(df))
    for y in years:
        print ("   Género más lento en ser leído en el año",str(y)+":", end=" ")
        print (practica.slowestGenreYear(df,y))

    # EJERCICIO 5
    print ("Ejercicio 5")
    dfalerts = practica.addAlerts(df)
    print ("b) Alertas en global:", end=" ")
    print (ordenaListaPorBloques(practica.showAlerts(dfalerts)))
    for y in years:
        print ("   Alertas en el año",str(y)+":", end=" ")
        print (ordenaListaPorBloques(practica.showAlertsYear(dfalerts,y)))

    # EJERCICIO 6
    print ("Ejercicio 6")
    print (practica.tooLate(dfalerts))

if __name__ == "__main__":
    main()

