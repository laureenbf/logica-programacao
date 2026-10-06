mais_5horas = 0
total_arrecadado = 0
total_veiculos = 0
tempo = int(input("Digite o tempo de permanência do veículo (0 para encerrar): "))

while  tempo != 0:
    if tempo <= 2:
        print("você ficou", tempo,"horas e deverá pagar R$8,00")
        total_arrecadado += 8
    elif tempo >= 3 and tempo <= 5:
        print("você ficou", tempo,"horas e deverá pagar R$15,00")
        total_arrecadado += 15
    else:
        print("você ficou", tempo,"horas e deverá pagar R$25,00")
        total_arrecadado += 25
        mais_5horas += 1
    total_veiculos += 1
    tempo = int(input("Digite o tempo de permanência do veículo (0 para encerrar): "))

print("O total de veículos foi,", total_veiculos," o total arrecadado foi", total_arrecadado, "reais e a quantidade de veículos que permaneceu por mais de 5 horas foi", mais_5horas)

