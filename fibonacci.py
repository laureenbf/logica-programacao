quantidade = int(input("digite a quantidade de termos que quer ver:"))


t1 = 0
t2 = 1

print("Sequência de Fibonacci:")
print(t1)
print(t2)

i = 3
while i <= quantidade:
    proximo = t1 + t2
    print(proximo)

    t1 = t2
    t2 = proximo
    i += 1

