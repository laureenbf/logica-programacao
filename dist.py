distancia = float(input(" digite a distãncia percorrida: "))
combustivel = float(input("digite a quantidade consumida de combustível em litros: "))
consumomedio = distancia / combustivel

if consumomedio >= 12:
    print("veículo econõmico")
else:
    print("veículo pouco econõmico")

print(consumomedio)
