# Agustin Avila
# tinto.avila@gmail.com
# 17/8/21
import csv

# Funcion que devuelve los datos del camion como una lista de diccionarios
def costo_camion(nombre_archivo):
    datos = []
    with open(nombre_archivo, 'rt') as f:
        costo_total = 0
        filas = csv.reader(f)
        headers = next(filas)    #Salta los datos de cabecera
        for n_fila, fila in enumerate(filas, start=1):
            record = dict(zip(headers, fila))
            try:
                ncajones = int(record['cajones'])
                precio = float(record['precio'])
                costo_total += ncajones * precio
                datos.append(record)
            # Esto atrapa errores en los int() y float() de arriba.
            except ValueError:
                print(f'Fila {n_fila}: No pude interpretar: {fila}')
    return datos

# Funcion que devuelve los datos de los precios como un diccionario
def leer_precios(nombre_archivo):
    datos = {}
    with open(nombre_archivo, 'rt') as f:
        rows = csv.reader(f)
        #headers = next(rows)    #Salta los datos de cabecera
        for row in rows:
            try:
                datos[row[0]] = row[1]
            except:
                pass    # Podria levantar alguna alerta, en este caso no hace nada
    return datos

def hacer_informe(cajones,precios):
    informe = []
    for item in cajones:
        if item['nombre'] in precios:   # Si la fruta está en el diccionario de precios, calcula la ganancia
            informe.append((item['nombre'],int(item['cajones']),float(item['precio']),float(precios[item['nombre']])))   
    return informe

# Nombres de archivos para abrir:
nombre_archivo_camion = '../Data/fecha_camion.csv'
nombre_archivo_precios = '../Data/precios.csv'

# Variables que almacenan los datos cargados de cada archivo:
camion = costo_camion(nombre_archivo_camion)
precios = leer_precios(nombre_archivo_precios)

informe = hacer_informe(camion,precios)
separador=str('').rjust(10,'-') 
headers = ('Nombre', 'Cajones', 'Precio', 'Cambio')
print(f'{headers[0]:>10s} {headers[1]:>10s} {headers[2]:>10s} {headers[3]:>10s}')
print(f'{separador} {separador} {separador} {separador}' )
for nombre, cajones, precio, cambio in informe:
    print(f'{nombre:>10s} {cajones:>10d} {("$"+"{:.2f}".format(precio)):>10s} {cambio:>10.2f}')
