nome=input("digite seu nome: ")
anos=int(input("digite sua idade em anos: "))
meses=int(input("digite quantos meses: "))
dias=int(input("digite quantidade de dias: "))
total_dias=(anos*365)+(meses*30)+dias
print("seu nome é",nome, "e você viveu aproximadamente", total_dias,"dias.")   