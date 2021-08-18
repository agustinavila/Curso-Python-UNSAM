# Agustin Avila
# tinto.avila@gmail.com
# 17/8/21

import csv

def costo_camion(nombre_archivo):
    costo = 0
    with open(nombre_archivo, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)    #Salta los datos de cabecera
        for line in rows:
            costo += int(line[1])*float(line[2]) #Va sumando el parcial de a una linea
    return costo

costo = costo_camion('../Data/camion.csv')
print('Costo total:', costo)