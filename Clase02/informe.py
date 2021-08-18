# Agustin Avila
# tinto.avila@gmail.com
# 17/8/21
import csv

# Funcion que devuelve los datos del camion como una lista de diccionarios
def costo_camion(nombre_archivo):
    datos = []
    with open(nombre_archivo, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)    #Salta los datos de cabecera
        for row in rows:
            lote = {'nombre': row[0], 'cajones': int(row[1]), 'precio': float(row[2])}
            datos.append(lote)
    return datos

# Funcion que devuelve los datos de los precios como un diccionario
def leer_precios(nombre_archivo):
    datos = {}
    with open(nombre_archivo, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)    #Salta los datos de cabecera
        for row in rows:
            try:
                datos[row[0]] = row[1]
            except:
                pass    # Podria levantar alguna alerta, en este caso no hace nada
    return datos

# Nombres de archivos para abrir:
nombre_archivo_camion = '../Data/camion.csv'
nombre_archivo_precios = '../Data/precios.csv'

# Variables que almacenan los datos cargados de cada archivo:
camion = costo_camion(nombre_archivo_camion)
precios = leer_precios(nombre_archivo_precios)


costo_camion = 0        # Inicializa las variables en cero
ganancia_venta = 0
for item in camion:
    costo_camion += item['cajones']*item['precio']  #Calcula el costo del item
    if item['nombre'] in precios:   # Si la fruta está en el diccionario de precios, calcula la ganancia
        ganancia_venta += item['cajones']*float(precios[item['nombre']])    #Calcula la ganancia del item


# Imprime por pantalla el resultado
print("El costo del camion es de",costo_camion)
print("El ingreso por la venta es de",ganancia_venta)
saldo_neto = ganancia_venta - costo_camion
print(f'El saldo final es de {saldo_neto:10.2f}')
if saldo_neto<0:
    print("Hubo pérdida!")
elif saldo_neto == 0:
    print("Ni se ganó ni se perdió")
else:
    print("Hubo ganancia!")
