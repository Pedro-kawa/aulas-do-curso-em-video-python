nomeC = str(input("Me diga seu nome completo: ")).title().strip()

#Primeiro nome
PN = nomeC.split()

#Ultimo nome
UN = PN[len(PN)-1]

print (PN [0], UN) 