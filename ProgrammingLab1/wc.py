def contarighe(nomefile):
    conta = 0
    for riga in open(nomefile):
    conta += 1
    return conta
print(contarighe('wc.py'))