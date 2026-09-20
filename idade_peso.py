soma_idade = 0
mais_90 = 0

for i in range(7):
    idade = int(input("Digite sua idade:"))
    peso = float(input("Digite seu peso: "))
    if peso > 90:
        mais_90 += 1
        
    soma_idade += idade


media = soma_idade / 7

print("a quantidade de pessoas com mais de 90 quilos foi: ", mais_90)
print("a média das idades das sete pessoas é:", media) 