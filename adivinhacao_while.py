numero_secreto = 27
i = 1
a = 1

while i != 27:
    i = int(input("tente acertar o número! : "))

    if i < 27:
        print("tente um valor maior!")
    elif i > 27:
        print("tente um valor menor!")
    else:
        print("parabéns! você acertou em ", a , "tentativas")
    a +=1

    
