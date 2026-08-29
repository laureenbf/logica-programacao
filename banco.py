idade = int(input("Digite sua idade: "))
renda = float(input("Digite sua renda: "))

if idade >= 18 and idade <= 65 and renda >= 2000:
    print("Aprovado!") 
else:
    print("Negado!")