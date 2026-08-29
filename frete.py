valortotal = float(input("digite o valor total da compra: "))

if valortotal >= 200: 
    frete = 0
    print("frete grátis!!")
else:
    frete = 20
    print("frete é 20 reais")

valorfinal = valortotal + frete

print("O valor final é", valorfinal)



#valorcompra = valorcompra + 20
#ou
#valorcompra +=20
#sao iguais!!!!#
