#%%
def buscar_u_elemento(lista,e):
    pos = -1  # comenzamos suponiendo que e no está
    for i, z in enumerate(lista): # recorremos la lista
        if z == e:   # si encontramos a e
            pos = i  # guardamos su posición
    return pos
# %%
def buscar_n_elemento(lista,e):
    cont = 0  # comenzamos suponiendo que e no está
    for z in lista: # recorremos la lista
        if z == e:   # si encontramos a e
            cont +=1  # guardamos su posición
    return cont
# %%
def maximo(lista):
    max = lista[0]  # comenzamos suponiendo que e no está
    for e in lista: # recorremos la lista
        if e > max:   # si encontramos a e
            max = e  # guardamos su posición
    return max
# %%
def minimo(lista):
    min = lista[0]  # comenzamos suponiendo que e no está
    for e in lista: # recorremos la lista
        if e < min:   # si encontramos a e
            min = e  # guardamos su posición
    return min