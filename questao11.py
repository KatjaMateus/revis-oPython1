frase = str(input("Digite uma frase: ")).strip()

contador = 0
contador2 = 0
for letra in frase:
    if letra in "aeiou":
        contador += 1
print(f"A frase tem {contador} vogais.")

for letra in frase:
    if letra in "bcdfghjklmnpqrstvwxz":
        contador2 += 1
print(f"A frase tem {contador2} consoantes.")
