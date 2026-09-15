soma = 0
venda_alta = 0

for i in range (5):
    valor = float(input("Digite o valor da venda: "))
    soma += valor

    if valor > 500: 
        print("venda alta!!!")
        venda_alta += 1

    elif valor >= 200:
        print("venda média!!")

    else:
        print("venda baixa!") 

   
print (" o total de vendas altas foi: " , venda_alta, "e o valor total das vendas foi: ", soma)