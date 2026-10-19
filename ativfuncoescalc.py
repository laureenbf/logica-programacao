def somar(a,b):
    print(a + b)

def subtrair(a,b):
    print(a - b)

def multiplicar(a,b):
    print(a * b)

def dividir(a,b):
    print(a / b)

num1 = int(input("digite o primeiro número: "))
num2 = int(input("digite o segundo número: "))
opera = input("digite a operação (+,-,*,/): ")

if opera == "+":
    print("resultado: ")
    somar(num1,num2)

elif opera == "-":
    print("resultado: ")
    subtrair(num1,num2)

elif opera == "*":
    print("resultado: ")
    multiplicar(num1,num2)

else:
    if num2 == 0:
        print("erro!!! divisão por 0!")
    else:
        print("resultado: ")
        dividir(num1,num2)