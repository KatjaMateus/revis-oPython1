frase = str(input("Digite uma frase: ")).strip()

contador = 0
for letra in frase:
    if letra in "aeiou":
        contador += 1

print(contador)