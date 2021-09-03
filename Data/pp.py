# Primero las dos funciones necesarias para leer los archivos
def leer_precios(nombre_archivo):
    import csv
    f = open(nombre_archivo)
    precio_frutal = {}
    for line in f:
        try:
            row = line.split(',')
            if len(row) >= 2:
                precio_frutal[f'{row[0]}'] = float(row[1][:-2])
        except:
            pass
    return precio_frutal

def leer_camion(nombre_archivo):
    import csv
    f = open(nombre_archivo)
    headers = next(f).split(',')
    camion_total=[]
    for line in f:
        camion= {}
        row = line.split(',')
        camion[headers[0]] = row[0]
        camion[headers[1]] = int(row[1])
        camion[headers[2][:-1]] = float(row[2][:-2])               
        camion_total.append(camion)
    return camion_total

# Generadora del balance
def balance():
# Generamos las listas para luego recorrerlas 
    precios = leer_precios('precios.csv')   
    camiones = leer_camion('camion.csv')
# Ganancia
    ganancia = 0
    for b in precios:
        for j in camiones:
            if j['nombre'] == b:
                ganancia +=  precios[j['nombre']] * j['cajones']
     
    # Costo Total del camion
    costo = 0.0
    for s in camiones:
        costo += s['cajones'] * s['precio']
        # print(s['cajones'])

    print(f"Su ganancia de este mes fue de {ganancia}, los gastos en los camiones fue de {costo}: ")
    print(f"Lo que da un balance de {ganancia-costo} ")

balance()