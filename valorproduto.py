preco = float(input("Digite o valor do produto: "))

if preco >= 100:
    desconto = preco * 0.10
    print("O preço final é", preco - desconto)
else:
    desconto = preco * 0.05
    print("o preço final é ", preco - desconto)