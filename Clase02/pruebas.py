# -*- coding: utf-8 -*-
"""
Created on Tue Aug 17 22:03:07 2021

@author: manue
"""

import csv

# Funcion que crea un diccionario con los precios de cada fruta
def leer_precio(nombre_archivo):
    f = open(nombre_archivo, 'r')
    rows = csv.reader(f)
    precios = {}
    for row in rows:
        try:
            precios[row[0]] = row[1]
        except:
            print('', end = '')
    f.close()
    return precios

# Funcion que crea una lista de tuplas de frutas con su cantidad de cajones y precio por cajon
def leer_camion(nombre_archivo):
    camion = []
    
    f = open(nombre_archivo)
    rows = csv.reader(f)
    headers = next(rows)
    
    for row in rows:
        lote = (row[0], int(row[1]), float(row[2]))
        camion.append(lote)
    
    f.close()
    return camion

# Llamo a las funciones y guardo sus valores
precios = leer_precio('../Data/precios.csv')
camion = leer_camion('../Data/camion.csv')

total = 0

for nombre, cajones, precio in camion:
        total += cajones * precio

'''
Recorro el diccionario y busco en toda la lista de tuplas donde los nombres de frutas coinciden
para hacer la cuenta de la venta con la cantidad de cajones que llegaron en el camion y 
el precio vendido al publico. Luego con el total del camion y la venta al publico, saco la ganancia
'''

venta = 0

for fruta, precio in precios.items():
    try:
        for nombre in camion:
            if fruta in nombre[0]:
                venta += float(precio) * int(nombre[1])
    except:
        print('', end='')
        
print('El total gastado es: ', total)
print('Lo obtenido en ventas es: ', venta)
print('La ganancia fue: %0.2f' % (venta - total))