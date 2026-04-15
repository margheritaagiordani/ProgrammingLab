# class Canguro():
#     def __init__(self):
#         self.contenuto_tasca = []

#     def intasca(self, oggetto):
#         self.contenuto_tasca.append(oggetto)

#     def __str__(self):
#         return f"Il canguro ha: {self.contenuto_tasca}"

# can = Canguro()
# guro = Canguro()

# can.intasca('wallet')
# print(can)
# print(guro)



# #lez05_es1
# class Veicolo():

#     def __init__(self, modello, marca, anno):
#         self.modello = modello
#         self.marca = marca
#         self.anno = anno
#         self.speed = 0

#     def __str__(self):
#         return ('veicolo "{}", "{}", "{}", "{}"'.format(self.modello, self.marca, self.anno, self.speed))
    
#     def accelerare (self): #metodo che incrementa di 5 l'attributo speed
#         self.speed += 5
    
#     def frenare (self):
#         self.speed = self.speed - 5 #analogo di accelerare

#     def get_speed (self): #metodo che ritorna l'attributo speed
#         return self.speed
    

# class Auto(Veicolo):

#     def __init__(self, modello, marca, anno, numero_porte):
#         super().__init__(modello, marca, anno)
#         self.numero_porte = numero_porte
    
#     def __str__(self):
#         return ('veicolo "{}", "{}", "{}", "{}", "{}"'.format(self.modello, self.marca, self.anno, self.speed, self.numero_porte))


# class Moto(Veicolo):

#     def __init__(self, modello, marca, anno, tipo):
#         super().__init__(modello, marca, anno)
#         self.tipo = tipo
    
#     def __str__(self):
#         return ('veicolo "{}", "{}", "{}", "{}", "{}"'.format(self.modello, self.marca, self.anno, self.speed, self.tipo))
    

# macchina = Auto('500', 'Fiat', '2006', '3')
# print(macchina)


# bike = Moto('ducati', 'rossa', '2980', 'sportiva')
# print (bike)


#lez05_es1

# class Persona():
    
#     def __init__(self, ruolo, nome, cognome):
#         self.ruolo = ruolo
#         self.nome = nome
#         self.cognome = cognome
    
#     def saluta(self):
#         print ('Ciao sono', self.ruolo + ',', self.nome, self.cognome)

# class Studente(Persona):
    
#     def __init__(self, ruolo, nome, cognome, corso, corsi_frequentati):
#         super().__init__('Studente UNITS', nome, cognome)
#         self.corso = corso
#         self.corsi_frequentati = []
    
#     def frequenta_corsi(self):
#         corso = input("Inserisci il corso che stai frequentando: ")
#         self.corsi_frequentati.append(corso)
#         print(self.corsi_frequentati) 
    
#     def saluta(self):
#         Persona.saluta(self)
#         print ("> Frequenta il corso:", self.corso)
    
#     def __str__(self):
#         return ('Persona "{}", "{}", "{}", "{}", "{}"'.format(self.ruolo, self.nome, self.cognome, self.corso, self.corsi_frequentati))
    

# studente1 = Studente('', 'marghe', 'gio', 'iada', '')
# studente1.frequenta_corsi()
# studente1.frequenta_corsi()
# print(studente1)

# class Docente(Persona):
#     def __init__(self, nome, cognome, corso, corsi_insegnati):
#         super().__init__("Docente UNITS", nome, cognome)
#         self.corso = corso
#         self.corsi_insegnati = []

#     def saluta(self):
#         Persona.saluta(self)
#         print(">Docente del corso: ", self.corso)

#     def insegna_corsi(self):
#         corso = input("Inserisci il corso che il docente insegna: ")
#         self.corsi_insegnati.append(corso)
#         print(self.corsi_insegnati) 

#     def __str__(self):
#         return ('Persona "{}", "{}", "{}", "{}", "{}"'.format(self.ruolo, self.nome, self.cognome, self.corso, self.corsi_insegnati))

# docente1= Docente('laura', 'nenzi', 'iada', '')    
# docente1.insegna_corsi()
# docente1.insegna_corsi()
# print(docente1)

#lez05_es4
class Poligono():

    def __init__(self, nlati):
        self.nlati = nlati

    def __str__(self):
        return ('Sono un poligono con "{}" lati', (self.nlati))
    
class Quadrilatero(Poligono):
    
    def __init__(self):
        super().__init__(nlati)
        self.nlati = 4

    def __str__(self):
        return ('Sono un quadrilatero')


class Rettangolo(Quadrilatero):

    def __init__(self, base, altezza):
        super().__init__()
        self.base = base
        self.altezza = altezza

    def __str__(self):
        return ('Sono un rettangolo con base "{}" e altezza "{}"'.format(self.base, self.altezza))
    
    def area(self):
        x = self.base * self.altezza
        return x
    
    def perimetro(self):
        y = 2*self.base + 2*self.altezza
        return y
    

class Triangolo(Poligono):
        
    def __init__(self, a, b, c):
        super().__init__()
        self.nlati = 3
        self.a = a
        self.b = b
        self.c = c


    def __str__(self):
        return ('Sono un triangolo con a = "{}", b = "{}", c = "{}"'. format(self.a, self.b, self.c))
    
    def perimetro(self):
        z = self.a + self.b + self.c
        return z

    def is_equilatero(self):
        if self.a == self.b == self.c:
            return True
        else:
            return False


quadrato = Rettangolo(2,2)
print(quadrato)
print(quadrato.area())
print(quadrato.perimetro())