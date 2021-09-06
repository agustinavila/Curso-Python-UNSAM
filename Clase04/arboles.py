#%%
import csv
from collections import Counter

#%%
def leer_arbol(nombre_archivo):
    types = [float, float, int, int, int, int, int, str, str, str, str, str, str, str, str, float, float]
    with open(nombre_archivo, 'rt', encoding="utf8") as f:
        filas = csv.reader(f)
        headers = next(filas)    #Salta los datos de cabecera
        datos = [{name: func(val) for name, func, val in zip(headers, types, row)} for row in filas]
    return datos
#%%
def alturas(arboleda,tipo_arbol):
    alt = [(float(arbol["altura_tot"]),float(arbol["diametro"])) for arbol in arboleda if arbol["nombre_com"] == tipo_arbol]
    return alt

# %%
def medidas_de_especies(especies,arboleda):
    salida = {especie: alturas(arboleda,especie) for especie in especies}
    return salida
# %%
