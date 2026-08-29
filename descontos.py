valordacompra = float(input("Digite o valor da compra: "))
cadastro = input("Vocẽ é cadastrado(sim ou não): ")

if (cadastro == "sim") and (valordacompra >= 500):
    desconto = 0.2 * valordacompra 
    valorfinal = valordacompra - desconto
    print ("O seu desconto foi de 20% e o valor final da compra foi", valorfinal)

elif (cadastro == "não") and (valordacompra >= 300):
    desconto = 0.1 * valordacompra  
    valorfinal = valordacompra - desconto
    print("O seu desconto foi de 10% e o valor final da compra foi:", valorfinal)

elif (cadastro == "sim") and (valordacompra >= 150):
    desconto = 0.05 * valordacompra
    valorfinal = valordacompra - desconto
    print("O seu desconto foi de 5% e o valor final da compra foi:", valorfinal)

else:
    print("Nenhum desconto na compra.")
