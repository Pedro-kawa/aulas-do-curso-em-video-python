import random
num = input("Eu pensei em um numero entre 0-5, tente adivinhar: ")

numEsc = random.randint(0,5)
t = (num.isalpha())
if t == True:
    print("Por favor apenas numeros")
else:

    if int(num) <= -1:
        print("Por favor não escolha um numero negativo")

    else: 
        
        if int(num) >= 6: 
            print("Por favor escolha um numero entre 0 e 5")

        
        else:
            
            if int(num) == int(numEsc):
                print("Você acertou, parabéns")
            #Se for diferente
            else:
                print("""Você errou infelizmente \no numero que escolhi foi {}""".format(numEsc))
