sum = 0

for nota in range(4):
    sum += float(input("Digite a nota: "))
    media = sum / 4

if media == 10:
    print("Aprovado com distinção")
elif media >= 7 and media < 10:
    print("Aprovado")
else:
    print("Reprovado")



