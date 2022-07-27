import random 
Alu_1 = input('Nome 1: ')
Alu_2 = input("Nome 2: ")
Alu_3 = input("Nome 3: ")
Alu_4 = input("Nome 4: ")

Alunos = [Alu_1, Alu_2, Alu_3, Alu_4]

escolhido = (random.choice(Alunos))
print("Parabéns {} você foi sorteado para apagar o quadro".format(str(escolhido)))