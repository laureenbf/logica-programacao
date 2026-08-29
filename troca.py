a=int(input("digite um valor para A: "))
b=int(input("digite um valor para B: "))

print("Antes da troca: A:",a,"B:",b)

a = a + b
b = a - b
a = a - b


print("Depois da troca: A:",a,"B:",b)