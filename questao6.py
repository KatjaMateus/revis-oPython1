num1 = (float(input("Digite o primeiro número: ")))
num2 = (float(input("Ditige o segundo número: ")))
operacao = str(input("Qual operação você quer fazer? [ soma = s | subtração = sub | multiplicação = m | divisão = d ]"))

s = num1 + num2
sub = num1 - num2
m = num1 * num2
d = num1 / num2

if operacao == "s":
    print(s)
    if s > 0:
        print(f'{s} é positivo')
    else:
        print(f"{s} é negativo")
    if s % 2 == 0:
        print(f"{s} é número par")
    else:
        print(f"{s} é número impar")


