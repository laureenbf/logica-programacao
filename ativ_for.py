pares = 0
impares = 0
for i in range (1,8):
    num = int(input("digite o número: "))
    if num % 2 == 0:
        pares += 1
    else:
        impares += 1
print("Foram", pares, "números pares e", impares, "números ímpares")

