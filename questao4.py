letra = str(input("Digite uma letra: ")).lower().strip()
if letra in "aeiou":
    print(f"A {letra} é vogal.")
elif letra in "bcdfghjklmnpqrstvxywz":
    print(f"A {letra} é consoante.")
else:
    print("Digite uma LETRA!")