#%%
import csv
from collections import Counter
import matplotlib.pyplot as plt
import numpy as np

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
# Cargar los datos y generar lista con datos de jacaranda
datos = leer_arbol("../Data/arbolado-en-espacios-verdes.csv")
alto_jacaranda = alturas(datos,"Jacarandá")

# %%
# Ej 5.25: Graficar histograma de alturas de jacaranda
def hist_altura(datos):
    altos =[dato[0] for dato in datos]
    plt.hist(altos,bins=20)
hist_altura(alto_jacaranda)
# %%
# Ej 5.26: grafico en coord cartesianas
def scatter_hd(datos):
    data_np = np.array(datos)
    plt.scatter(data_np[:,0],data_np[:,1], alpha = 0.1)
    plt.xlabel("diametro (cm)")
    plt.ylabel("alto (m)")
    plt.title("Relación diámetro-alto para Jacarandás")
scatter_hd(alto_jacaranda)
# %%
