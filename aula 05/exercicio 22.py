from ntpath import join
from posixpath import split

#Nome completo.
nome = input("Qual seu nome completo: ")

#nome em minusculo/maiosculo.
Maior = nome.upper()
Menor = (nome.lower())

#nome sem considerar os espaços/caracterias.
Qtl = (nome.split())
Qtl1 = "".join(Qtl)
Qtl2 = len(Qtl1)

#Primeiro nome/caracterias.
Pn = nome.split()
Pn = Pn[0]
Pn1 = len(Pn)

print("""\nseu nome em maiúsculo é:\n{}\n\nseu nome em minúsculo é:\n{}\n\nSeu nome possue {} caracterias
\nO primeiro nome tem {} caracterias""".format(Maior,  Menor, Qtl2, Pn1))