maior_dez = 0
a = 0
b = 0

for i in range (6):
    num = int(input("digite o número: "))

    if i == 0:
        a = num
        b = num


    if a < num:
        a = num
    else:
        a = a


    if b > num:
        b = num
    else:
        b = b



    if num > 10:
        maior_dez += 1
    else:
        maior_dez = maior_dez
    
print( "o maior número foi: ", a)
print( "o menor número foi: ", b)
print("a quantidade de números maiores que 10 foi: ", maior_dez)

