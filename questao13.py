while True:
    senha = str(input("Digite sua senha: "))
    if len(senha) >= 8 and len(senha) <= 12:
        print(senha)
        break
    else:
        print("Tente novamente")