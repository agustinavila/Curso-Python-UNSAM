vocales = 'aAeEiIoOuU'
print("Este programa devuelve la frase que se le provea, pero en geringoso.")
frase = str(input("Por favor, ingrese una frase: "))
frase_gerin = ''
for caracter in frase:
    frase_gerin = frase_gerin + caracter
    if caracter in vocales:
        frase_gerin = frase_gerin + 'p' + caracter.lower()

print(frase_gerin)