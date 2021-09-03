#%%
import csv
from collections import Counter

def leer_parque(nombre_archivo, parque):
    datos = []
    with open(nombre_archivo, 'rt') as f:
        filas = csv.reader(f)
        headers = next(filas)    #Salta los datos de cabecera
        for n_fila, fila in enumerate(filas, start=1):
            record = dict(zip(headers, fila))
            if record['espacio_ve']==parque:
                try:
                    datos.append(record)
                # Esto atrapa errores en los int() y float() de arriba.
                except ValueError:
                    print(f'Fila {n_fila}: No pude interpretar: {fila}')
    return datos
#%%
def especies(lista_arboles):
    set_unicas = set(tuple(entrada["nombre_com"] for entrada in lista_arboles))
    return set_unicas
# %%

def contar_ejemplares(lista_arboles):
    cant_arboles = Counter()
    for arbol in lista_arboles:
        cant_arboles[arbol["nombre_com"]] += 1
    
    return cant_arboles.most_common(5)
# %%

def obtener_alturas(lista_arboles, especie):
    datos = []
    for arbol in lista_arboles:
        if arbol['nombre_com']==especie:
                datos.append(float(arbol["altura_tot"]))
    return datos
# %%
def obtener_inclinaciones(lista_arboles,especie):
    datos = []
    for arbol in lista_arboles:
        if arbol['nombre_com']==especie:
                datos.append(float(arbol["inclinacio"]))
    return datos

#%%
def especimen_mas_inclinado(lista_arboles):
    record = dict(zip(lista_arboles, fila))