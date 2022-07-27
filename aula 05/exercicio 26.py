from itertools import count

#Sua frase
nome = str(input("Digite uma frase: ")).strip()

#Quantos (A) tem em sua frase
QA = nome.upper().count("A")

#Quando aparece a primera vez
QC = nome.upper().find("A")

#Quando aparece a ultima vez
QT = nome.upper().rfind("A")


print("""A letra (A) aparece {} vezes em sua Frase
A letra (A) aparece pela primeira vez na {}° caracteria
A Letra (A) aparece pela ultima vez na {}° carateria""".format(QA, QC+1, QT+1))
