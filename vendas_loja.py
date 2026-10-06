venda = float(input("Digite o valor da venda:"))
total_vendas = 0
valor_total = 0
vendas_maior200 = 0

while venda != 0:
    if venda >=200:
        venda_final = venda - (venda * 0.1)
        vendas_maior200 += 1
        print("A venda receberá 10% de desconto. O valor final da venda foi:", venda_final)
        total_vendas += 1
        valor_total += venda
    else:
        print("O valor da venda foi:", venda)
        total_vendas += 1
        valor_total += venda

    venda = float(input("Digite o valor da venda:"))

print("O total de vendas foi", total_vendas)
print("O valor total das vendas (sem desconto) foi de:", valor_total)
print("O número de vendas maiores que 200 foi", vendas_maior200)
