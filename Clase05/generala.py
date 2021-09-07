#%% imports
import random
from collections import Counter

#%% tira una cantidad de dados dada
def tirar(cant_dados):
    tirada=[]
    for i in range(cant_dados):
        tirada.append(random.randint(1,6)) 
    return tirada

#%% Funcion para comprobar si la tirada es una generala
def es_generala(tirada):
    num = tirada[0]
    for dado in tirada:
        if dado != num:
            return False
    return True

# %% funcion que realiza hasta 3 tiradas para intentar obtener generala

def jugar():    
    dados = tirar(5)
    for i in range(2):
        if not es_generala(dados):
            cont = Counter(dados).most_common()
            mas_comun = cont[0]
            if mas_comun[1] ==1:
                dados_nuevos = tirar(5)
            else:
                dados_nuevos = tirar(5-mas_comun[1])
            j=0
            for ind,valor in enumerate(dados):
                if valor != mas_comun[0]:
                    dados[ind] = dados_nuevos[j]
                    j += 1
        else:
            break
    return es_generala(dados)

# %% función que devuelve la probabilidad de obtener una generala
def prob_generala(N):
    G = 0
    for jugada in range(N):
        if jugar():
            G += 1
    prob = G/N
    return prob

#%% la misma funcion que el caso anterior, solo que en caso de ser todos distintos, guarda uno y tira 4
def jugar2():
    dados = tirar(5)
    for i in range(2):
        if not es_generala(dados):
            cont = Counter(dados).most_common()
            mas_comun = cont[0]
            dados_nuevos = tirar(5-mas_comun[1])
            j=0
            for ind,valor in enumerate(dados):
                if valor != mas_comun[0]:
                    dados[ind] = dados_nuevos[j]
                    j += 1
        else:
            break
    return es_generala(dados)
# %%
def prob_generala_comp(N):
    G1 = 0
    G2 = 0
    for jugada in range(N):
        if jugar():
            G1 += 1
        if jugar2():
            G2 += 1

    prob1 = G1/N
    prob2 = G2/N
    return prob1,prob2

#%%
# Pequeño código para comparar qué caso es mejor
# Se realiza el 
for i in range(100): 
    caso1= 0
    v1,v2 = prob_generala_comp(10000)
    if v1 > v2:
        caso1 += 1
if caso1 < 50:
    print("Hay mas posibilidades de ganar guardando un dado")
elif caso1==50:
    print("Es lo mismo de cualquier manera")
else:
    print("Hay mas posibilidades de ganar cambiando todos los dados")

# Se corrió este experimento unas 10 veces, en todos los casos resultaba mejor guardar un dado
# Es decir, 10 veces se hicieron 100 experimentos viendo la probabilidad en cada caso de obtener generala tirando 10000 veces