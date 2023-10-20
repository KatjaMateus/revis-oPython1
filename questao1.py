numero1 = int(input("Ditige o primeiro numero :"))
numero2 = int(input("Ditige o segundo numero :"))
numero3 = int(input("Ditige o terceiro numero :"))

if numero1 >= numero2 and numero1 >= numero3:
    print(f"O maior número é {numero1}")
elif numero2 >= numero1 and numero2 >= numero3:
    print(f"O maior número é {numero2}")
else:
    print(f"O maior número é {numero3}")