def exibir_menu():
    print("1- comprar ingressos ")
    print("2- consultar ingressos disponíveis")
    print("3- mostrar tabela de preços")
    print("0- sair")

def calcular_valor(quantidade):
    return quantidade * 15

def comprar_ingressos(disponiveis,quantidade):
    if quantidade > 0 and quantidade <= disponiveis:
        disponiveis = disponiveis - quantidade
        print("O valor foi", calcular_valor(quantidade))
        print("restaram", disponiveis,"ingressos")
        return disponiveis
    else:
        print("só há", disponiveis,"ingressos disponíveis")
        return disponiveis

disponiveis = 30

opcao = int(input("digite a opção que vc deseja (0,1,2,3,): "))

while opcao != 0:
    
    if opcao == 1:
        quantidade = int(input("digite a quantidade: "))
        comprar_ingressos(disponiveis,quantidade)
        if quantidade > 0 and quantidade <= disponiveis:
             disponiveis = disponiveis - quantidade

    elif opcao == 2:
        print(disponiveis)

    elif opcao == 3:
        i = 1
        for i in range (1,6):
            print(i ,"ingressos =", calcular_valor(i), "reais")

    else:
        print("opção inválida")

    exibir_menu()

    opcao = int(input("digite a opção que vc deseja (0,1,2,3,): "))

print("programa encerrado")

            
            





