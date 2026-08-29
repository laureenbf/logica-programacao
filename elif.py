resultado = input("resultado da partida (V, E, D): ")

if resultado == "V":
    pontos = 3
elif resultado == "E":
    pontos = 1
else:
    pontos = 0

print("O time conquistou", pontos, "pontos")