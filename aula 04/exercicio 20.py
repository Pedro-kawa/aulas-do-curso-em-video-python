from binascii import a2b_base64


import random
A1 = input("Nome 1: ")
A2 = input("Nome 2: ")
A3 = input("Nome 3: ")
A4 = input("Nome 4: ")

lista = [A1, A2, A3, A4]

random.shuffle(lista)

print("A ordem sorteada foi\n{}".format(lista))
