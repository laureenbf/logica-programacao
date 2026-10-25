def calcular_bonus(salario):
    if salario <= 2000:
        return  0.15 * salario
    else:
        return 0.1 * salario


def salario_final(salario,calcular_bonus):
    return salario + calcular_bonus(salario)


def exibir_pagamento(nome,salario_final):
    print("O nome do funcionário é", nome, "e o seu salário final é", salario_final(salario,calcular_bonus))


nome = input("Digite o nome do funcionário: ")

salario = float(input("Digite o salário do funcionário: "))

calcular_bonus(salario)

salario_final(salario,calcular_bonus)

exibir_pagamento(nome,salario_final)