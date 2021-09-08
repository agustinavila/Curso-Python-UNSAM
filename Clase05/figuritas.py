# %%
import random
import numpy as np

# %% 
# Ej 5.10: crear
def crear_album(figus_total):
    album = np.array(np.zeros(figus_total))
    return album

# %%
# Ej 5.11: incompleto
def album_imcompleto(A):
    incompleto = 0 in A
    return incompleto

# %%
# ej 5.12: Comprar
def comprar_figu(figus_total):
    return random.randint(0,figus_total-1)
# %%
# Ej 5.13: cantidad de compras
def cuantas_figus(figus_total):
    album = crear_album(figus_total)
    incompleto = True
    cont = 0
    while incompleto:
        figu = comprar_figu(figus_total)
        album[figu] +=1
        incompleto = album_imcompleto(album)
        cont += 1
    return cont
# %%
# Ej 5.14/ 5.15: X repeticiones de Y figuritas
def repetir_album(rep,fig):
    resultados = np.array(np.empty(rep))
    for i in range(rep):
        resultados [i] = cuantas_figus(fig)
    promedio = np.mean(resultados)
    return promedio
# %%

prueba_5_15 = repetir_album(100,670)
# prueba_5_15 = 4634.83
# %%
# Ej 5.16: paquetes
def comprar_paquete(figus_total,figus_paquete):
    figus = np.array(np.zeros(figus_paquete))
    for i in range(figus_paquete):
        figus[i] = random.randint(0,figus_total-1)
    figus = figus.astype(int)
    return figus

# %%
# Ej 5.18: cuantos paquetes
def cuantos_paquetes(figus_total,figus_paquete):
    album = crear_album(figus_total)
    incompleto = True
    cont = 0
    while incompleto:
        paquete = comprar_paquete(figus_total,figus_paquete)
        for figu in paquete:
            album[figu] +=1
        incompleto = album_imcompleto(album)
        cont += 1
    return cont
# %%
# Ej 5.19: hacer n repeticiones:
def repetir_album_paq(rep,fig,paq):
    resultados = np.array(np.empty(rep))
    for i in range(rep):
        resultados [i] = cuantos_paquetes(fig,paq)
    promedio = np.mean(resultados)
    return promedio
# %%
print("se necesitan un promedio de",repetir_album_paq(100,670,5)," paquetes para completar un album de 670 comprando de a 5 figuritas")
# %%
