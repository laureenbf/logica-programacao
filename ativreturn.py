def calcular_media(n1,n2,n3):
    return (n1+n2+n3)/3

def verificar_situacao(calcular_media):

    if calcular_media  >= 7:
        return "aprovado"
    
    elif calcular_media  >= 5:
        return "recuperação"
    
    else:
        return "reprovado"
    
def exibir_resultado(nome,media,verificar_situacao):
    print("o nome do aluno é", nome, "a média dele foi", calcular_media(n1,n2,n3), "e a sua situação é", verificar_situacao(calcular_media(n1,n2,n3)))


nome = input("Digite o nome do aluno: ")

n1 = float(input("Digite a nota 1: "))
n2 = float(input("Digite a nota 2: "))
n3 = float(input("Digite a nota 3: "))



verificar_situacao(calcular_media(n1,n2,n3))

exibir_resultado(nome,calcular_media,verificar_situacao)