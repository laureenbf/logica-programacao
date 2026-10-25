total = 0

def calcular_subtotal(preco,quantidade):
    return  preco * quantidade

def calcular_troco(valor_pago,total):
    return valor_pago - total

def exibir_conta(nome,total,valor_pago,troco):
    print("O nome do cliente é", nome, "o total da compra foi de R$", total, "O valor pago foi", valor_pago, "e o troco do cliente foi R$", calcular_troco(valor_pago,total))

nome = input("digite seu nome:")

i = 0

while i < 1:
    preco = float(input("digite o preço: "))
    quantidade = int(input("digite a quantidade: "))
    continuar = input("deseja continuar? (s/n): ")

    calcular_subtotal(preco,quantidade)
    total += calcular_subtotal(preco,quantidade)

    if continuar == "n":
        i = 1


valor_pago = float(input("digite o valor pago: "))

while valor_pago < total:
    print("valor insuficiente")
    valor_pago = float(input("digite o valor pago: "))


calcular_troco(valor_pago,total)
exibir_conta(nome,total,valor_pago,calcular_troco(valor_pago,total))