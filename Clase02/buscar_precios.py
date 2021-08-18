# Agustin Avila
# tinto.avila@gmail.com
# 17/8/21

def buscar_precio(fruta):
    encontrado = False  #Flag para analizar si se encontró el resultado o no
    with open('../Data/precios.csv', 'rt') as f:
        for line in f:                          #Se lee linea por linea
            row = line.split(',')               #Se parsea la linea por comas
            if row[0].lower() == fruta.lower(): #Se sacan las mayusculas para "normalizar" la comparacion
                print("El precio de un cajon de "+ row[0] + " es: "+row[1])
                encontrado = True
                break
    if not encontrado:
        print("No se encontró la fruta ingresada...")

buscar_precio(str(input("Ingrese una fruta: ")))