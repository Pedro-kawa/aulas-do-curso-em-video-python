from dbm import ndbm
from gettext import find


Ndc = str(input("Me diga um nome de uma cidade e eu o direi se começa com santo ou não: ")).strip()
print(Ndc[:5].lower() == "santo")



