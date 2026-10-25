total = 0
desconto = 0
final = 0

def calcular_total(preco,quantidade):
    total = preco * quantidade
    print("O valor total da compra foi R$", total)

def calcular_desconto(total):
    if total < 100:
        print("sem desconto")
    elif total < 300:
        desconto = 0.05 * total
        print("o seu desconto foi de", desconto)
    else:
        desconto = 0.1 * total
        print("o seu desconto foi de", desconto)

def exibir_resumo(produto,total,desconto):
    print("O seu produto foi", produto, "o total original foi de R$", total , "e o valor final a ser pago é", total - desconto)

produto = input("digite o produto: ")
preco = float(input("digite o preço: "))
quantidade = int(input("digite a quantidade: "))

calcular_total(preco,quantidade)

total = preco * quantidade

calcular_desconto(total)

if total < 100:
    desconto = 0
elif total < 300:
    desconto = 0.05 * total    
else:
    desconto = 0.1 * total
        

exibir_resumo(produto,total,desconto)

