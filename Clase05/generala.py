#%% 
# imports
import random
from collections import Counter

#%% 
# tira una cantidad de dados dada
def tirar(cant_dados):
    tirada=[]
    for i in range(cant_dados):
        tirada.append(random.randint(1,6)) 
    return tirada

#%% 
# Funcion para comprobar si la tirada es una generala
def es_generala(tirada):
    num = tirada[0]
    for dado in tirada:
        if dado != num:
            return False
    return True

# %% 
# funcion que realiza hasta 3 tiradas para intentar obtener generala

def jugar():    
    dados = tirar(5)        # Realiza una primer tirada de 5 dados
    for i in range(2):      # y se puede relanzar 2 veces mas
        if not es_generala(dados):  #En caso de no ser generala, cambia dados
            cont = Counter(dados).most_common() # Cuenta los valores
            mas_comun = cont[0]                 # Obtiene una tupla de valor, cant del mas comun
            if mas_comun[1] ==1:                # Si la cantidad del mas comun es 1, son todos distintos
                dados_nuevos = tirar(5)         # Entonces se tira todo nuevamente
            else:                               # Si no, tira de vuelta una cantidad opuesta a los mas repetidos
                dados_nuevos = tirar(5-mas_comun[1])
            j=0                 # pequeño indice para recorrer los dados nuevos
            for ind,valor in enumerate(dados):
                if valor != mas_comun[0]:       # Si el valor no es el mas comun, se reemplaza por la nueva tirada
                    dados[ind] = dados_nuevos[j]
                    j += 1      # Se incrementa el contador para acceder al siguiente indice de la nueva tirada
        else:
            break               # Si es generala deja de tirar
    return es_generala(dados)   # Devuelve una comprobacion de si es generala o no

# %% 
# función que devuelve la probabilidad de obtener una generala
def prob_generala(N):
    G = 0
    for jugada in range(N):
        if jugar():
            G += 1
    prob = G/N
    return prob

#%% 
# la misma funcion que el caso anterior, solo que en caso de ser todos distintos, guarda uno y tira 4
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
# Función para comparar el rendimiento de ambas formas de jugar en caso de dados distintos
def prob_generala_comp(N):
    G1 = 0              #Contadores de exito para ambos casos
    G2 = 0
    for jugada in range(N):
        if jugar():     #Juega reponiendo todos
            G1 += 1
        if jugar2():    #Juega guardando uno
            G2 += 1

    prob1 = G1/N
    prob2 = G2/N
    return prob1,prob2  # Devuelve ambas probabilidades

#%%
# Pequeño código para comparar qué caso es mejor
caso1= 0                # Cantidad de veces que reemplazar todo es mejor que guardar uno
for i in range(100):    # Ejecuta el experimento 100 veces
    v1,v2 = prob_generala_comp(10000)   # Realiza 10k pasadas
    if v1 > v2:
        caso1 += 1
if caso1 < 50:          # Como se ejecuta 100 veces, se toma el 50 como punto medio
    print("Hay mas posibilidades de ganar guardando un dado")
elif caso1==50:
    print("Es lo mismo de cualquier manera")
else:
    print("Hay mas posibilidades de ganar cambiando todos los dados")

# Se corrió este experimento unas 10 veces, en la mayoria de los casos fue mejor guardar un dado
# Es decir, 10 veces se hicieron 100 experimentos viendo la probabilidad en cada caso de obtener generala tirando 10000 veces
# %%
