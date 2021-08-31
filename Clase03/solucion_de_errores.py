#solucion_de_errores.py
#Ejercicios de errores en el código
#%%
#Ejercicio 3.1. Función tiene_a()
#Comentario: El error se debía a que sólo evaluaba el primer caracter
#   Si o si devolvia True o False, y tampoco incrementaba el contador.
#   Por otro lado, sólo toma la letra 'a' minuscula, si bien se puede
#   tomar asi, se considera mejor agregar la mayuscula.
#   A continuación va el código corregido
def tiene_a(expresion):
    n = len(expresion)
    i = 0
    while i<n:
        if expresion[i] == 'a':
            return True
        elif expresion[i] == 'A':
            return True
        else:
            i += 1
    return False

print(tiene_a('UNSAM 2020'))

print(tiene_a('abracadabra'))
print(tiene_a('La novela 1984 de George Orwell'))
# %%
#Ejercicio 3.2. Función tiene_a()
#Comentario: El error se debía a problemas de sintaxis, le faltaban
#   varios ':', y la comparación tenia un operador = simple, en vez
#   de un operador == (doble). Finalmente devolvia 'Falso' en vez de 'False'
#   A continuación va el código corregido
def tiene_a(expresion):
    n = len(expresion)
    i = 0
    while i<n:
        if expresion[i] == 'a':
            return True
        i += 1
    return False

print(tiene_a('UNSAM 2020'))
print(tiene_a('La novela 1984 de George Orwell'))
# %%
#Ejercicio 3.3. Función tiene_1()
#Comentario: El error se debía a problemas de tipos. No se aseguraba
#   que la expresión fuera un string, por lo que al pasarle un numero
#   el código fallaba.
#   A continuación va el código corregido
def tiene_uno(expresion):
    expresion = str(expresion)
    n = len(expresion)
    i = 0
    tiene = False
    while (i<n) and not tiene:
        if expresion[i] == '1':
            tiene = True
        i += 1
    return tiene


print(tiene_uno('UNSAM 2020'))
print(tiene_uno('La novela 1984 de George Orwell'))
print(tiene_uno(1984))
# %%
#Ejercicio 3.4. Función suma()
#Comentario: El error se debía a que la función no devolvía ningun
#   valor, por lo tanto 'c' no tenía ningún valor.
#   A continuación va el código corregido
def suma(a,b):
    c = a + b
    return c

a = 2
b = 3
c = suma(a,b)
print(f"La suma da {a} + {b} = {c}")
# %%
#Ejercicio 3.5. Función leer_camion()
#Comentario: El error se debía a que siempre copiaba "por referencia"
#   el último valor, es decir, todos los valores de la lista
#   apuntaban a la misma dirección de memoria.
#   A continuación va el código corregido
import csv
from pprint import pprint
import copy

def leer_camion(nombre_archivo):
    camion=[]
    registro={}
    with open(nombre_archivo,"rt") as f:
        filas = csv.reader(f)
        encabezado = next(filas)
        for fila in filas:
            registro[encabezado[0]] = fila[0]
            registro[encabezado[1]] = int(fila[1])
            registro[encabezado[2]] = float(fila[2])
            camion.append(copy.deepcopy(registro))
    return camion

camion = leer_camion('../Data/camion.csv')
pprint(camion)
