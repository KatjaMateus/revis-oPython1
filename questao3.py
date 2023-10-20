sexo = str(input("""
    Digite o sexo:  [ M | F ]
    f - feminino
    m - masculino
                    """)).upper()

if sexo == "F":
    print("Feminino")
elif sexo == "M":
    print("Masculino")
else:
    print("Resposta inválida")