soma = 0
aprovados = 0
recuperacao = 0
reprovado = 0

for i in range (8):
    nota = float(input("Digite a nota do aluno: "))
    soma += nota
    if nota >= 7:
        aprovados += 1
    elif nota >= 5 and nota <=7:
        recuperacao += 1
    else:
        reprovado += 1

media = soma/8
print("a média da turma foi",media,",",aprovados," alunos estão aprovados,", recuperacao, "alunos estão de recuperação e", reprovado ,"alunos estão reprovados!!!")

