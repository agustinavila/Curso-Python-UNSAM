# Agustin Avila
# tinto.avila@gmail.com
# 17/8/21

def conversor_geringoso(palabra):
    vocales = 'aAeEiIoOuU'
    palabra_gerin = ''
    for caracter in palabra:
        palabra_gerin += caracter
        if caracter in vocales:
            palabra_gerin += 'p' + caracter.lower()
    return palabra_gerin

print("Este programa genera un diccionario de palabras con su equivalente en geringoso.")
frase = str(input("Por favor, ingrese una frase: "))
palabras = frase.split(" ") # Genera una lista con las palabras de la frase
palabras_dict = {}          # Genera el diccionario vacio
for palabra in palabras:
    palabras_dict[palabra] = conversor_geringoso(palabra)   # Asigna a cada palabra su equivalente geringoso
print(palabras_dict)

# Ejemplo de salida:
# Por favor, ingrese una frase: banana manzana mandarina
# {'banana': 'bapanapanapa', 'manzana': 'mapanzapanapa', 'mandarina': 'mapandaparipinapa'}
