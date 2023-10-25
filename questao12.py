soma = 0
while True:
    produto = str(input("Digite o nome do produto: "))
    preco = float(input("Digite o preço do produto: "))
    soma += preco
    print(soma)
    if preco == 000:
        break