nota1 = int(input("Digite a primeira nota: "))
nota2 = int(input("Digite a segunda nota: "))
media = 0

def calcular_media(nota1,nota2):
    media = (nota1+nota2)/2
    print("a média do aluno foi", media)
    
    if media >= 7:
        print("o aluno foi aprovado")
    else:
        print("o aluno foi reprovado")

calcular_media(nota1,nota2)

