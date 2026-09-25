c = int(input("Digite a capacidade da cabine: "))
a = int(input("Digite o número total de alunos na turma: "))
i = 1

if 2 <= c <= 100 and 1 <= a <= 1000:
  while (c-1) < a:
    a = a - (c-1) 
    i += 1


print("O número mínimo de viagens do teleférico para levar todos os alunos até o pico da montanha é:", i)