# from pickletools import pylist


# print ('hello world')
# print('ciao', 'gigi', sep=' ', end='.')
# var1 = 5
# var2 = 4
# print(f'\n{var1}, {var2}')
# print('{}, {}'.format(var1, var2))
# for i in range(10):
#     print (i)

# mylist = [1,2,3,4,5,6,7,8,9]

# for i, item in enumerate(mylist):
#     print('posizione{}:{}'.format(i,item))

# def orario (numero):
#     ore = int(numero/60)
#     min = int(((numero/60)-ore)*60)
#     print('{}:{}'.format(ore,min))
#     return 0

#n = int(input())
# orario(n)


# def is_pari(numero):
#     if (numero%2==0):
#         print('true')
#         return True
#     else:
#         print('false')
#         return False

# is_pari(n)

# def funzione(parola, lettera):
#     contatore = 0
#     for item in parola:
#         if (item == lettera):
#             contatore+=1
#     print(f'{contatore}')
#     return contatore

# mylist = 'banana'
# funzione(mylist, 'a')

# data = '2025-03-02'
# parti = data.split(sep='-')
# print(parti)

# my_file = open('shampoo.csv', 'r')
# for line in my_file:
#     print(line)

# my_file.close
# import os 
# cwd = os.getcwd()
# print(cwd)

#es_file
def sum(lista):
    x=0
    for elem in lista:
        x=x+elem
    print(x)
    return x

# my_list = [1,2,3,4,5]
# # sum(my_list)
# my_list2 = [1,2,3,4,3,2,1]

def is_palindromo(lista):
    length = len(lista)
    lista2=[]

    while(length!=0):
        lista2.append(lista[length-1])
        length-=1
    
    for elem1, elem2 in zip(lista, lista2):
        if(elem1 == elem2):
            print ('True')
            return True
        else:
            print ('False')
            return False

# is_palindromo(my_list)
# is_palindromo(my_list2)

def is_palindormo2(lista):
    lista2 = lista[::-1]
    print(lista==lista2)
    return (lista==lista2)

# is_palindormo2(my_list)
# is_palindormo2(my_list2)

def scambia(lista, i, j): #indici >= 1
    print(lista)
    lista[i-1], lista[j-1] = lista[j-1], lista[i-1]
    print(lista)

# scambia(my_list, 2,3)

def almeno_uno(lista1, lista2):
    flag = False
    for elem1 in lista1:
        for elem2 in lista2:
            if elem1==elem2:
                flag = True
                break
    print(flag)
    return(flag)

# almeno_uno(my_list, my_list2)

# my_dict = {0:'zero', 1:'uno', 2:'due', 3:'tre', 4:'quattro', 5:'cinque', 6:'sei', 7:'sette', 8:'otto', 9:'nove'}

def numeri_to_parole(dict, lista):
    lista2 = []
    for elem in lista:
        lista2.append(dict[elem])
    print(lista2)
    return(lista2)

#numeri_to_parole(my_dict, my_list)

def conteggio_occorrenze(lista):
    dict = {}
    for element in lista:
        counter = 1
        for i in lista[element:]:
            if (element==i):
                counter+=1
        dict[element]=counter
    print(dict)
    return (dict)

# print(my_list2)
# conteggio_occorrenze(my_list2)

def somma_valori(path):
    file = open(path, 'r')
    sum=0
    next(file)

    for line in file:
        lista= line.strip().split(',') #split() splits a string to a list; you can specify th separator, default: whitespace; strip() deletes white blankets at the beginning and at the end of the line
        valore = float(lista[1]) #ho lista fatta di data e numero, quindi per accedere al numero accedo al secondo elemento, indice 1!
        sum+=valore

    file.close()

    print(sum)
    return(sum)

#somma_valori('shampoo.csv')

def conta_valori_alti(path, soglia):
    counter=0
    with open(path, 'r') as file:
        next(file)
        for line in file:
            lista=line.strip().split(',')
            valore = float(lista[1])
            if (valore>soglia):
                counter+=1
    print(counter)
    return(counter)

#conta_valori_alti('shampoo.csv', 160.0)

def conta_occorrenze(path, word):
    counter=0
    with open(path, 'r') as file:
        lista=file.read().split(' ') #devi leggere il file le righe!!--> con il for line in file leggi già, quindi non serve mettere .read()
        for element in lista:
            if (element==word):
                counter+=1
    print(counter)
    return(counter)

#conta_occorrenze('file_prova.txt', 'tutto')

def conteggio(path):
    dict = {}
    with open(path, 'r') as file:
        list = file.read().strip().split()
        for index, element in enumerate(list):
            counter=1
            if(element not in dict):
                for i in list[index+1:]:
                    if (element==i):
                        counter+=1
                dict[element]=counter
    print(dict)
    return(dict)

# conteggio('file_prova.txt')

def rimuovi(path):
    list = []
    with open (path, 'r') as input:
        for line in input: #ATTENTA!!! così stai già leggendo! non ti serve fare .read()!!!!!!!
            element = line
            if (element not in list):
                list.append(element)
    
    with open('unique.txt', 'w') as output:
        for index, element in enumerate(list):
            output.write("".join(list[index]))

# rimuovi('file_prova.txt')

import random

class Coin():

    def __init__(self, faccia=None): #posso mettere a None la faccia inizialmente e deciderla solo post .lancia(), così non devo passargli la faccia
        self.faccia = faccia

    def __str__(self):
        return ('faccia {}'.format(self.faccia))
    
    def lancia(self):
        random_number = random.randint(0,1)
        if (random_number==1):
            self.faccia='testa'
        else:
            self.faccia='croce'

# moneta = Coin()
# moneta.lancia()
# print(moneta)

class Veicolo():

    def __init__(self, modello, marca, anno, speed=0):
        self.modello = modello
        self.marca = marca
        self.anno = anno
        self.speed = speed
    
    def __str__(self):
        return ('Veicolo "{}","{}","{}","{}"'.format(self.modello, self.marca, self.anno, self.speed))
    
    def accelerare(self):
        self.speed+=5
    
    def frenare(self):
        self.speed-=5
    
    def get_speed(self):
        print('speed attuale del veicolo:"{}"'.format(self.speed))

# car_A = Veicolo('c3', 'citroen', '2006')
# print(car_A)
# car_A.accelerare()
# car_A.get_speed()
# car_A.frenare()
# car_A.get_speed()

# class CSVFile():
#     def __init__(self, name): 
#         self.name = name
#         try:
#             with open(name, 'r') as file:
#                 file.readline()
#         except FileNotFoundError as e:
#             print(f'da __init__() file non trovato, ho avuto un {type(e)}')
    
#     def get_data(self):
#         list = []
        
#         try: 
#             with open(self.name, 'r') as file:
#                 next(file)
#                 for line in file:
#                     list.append(line.strip())
#                 print(list)
#                 return list
#         except FileNotFoundError as e:
#             print(f'da get_data() file non trovato!, ho avuto un {type(e)}')


# csv = CSVFile('shampoo.csv')
# csv.get_data()
class ParameterError(Exception):
    pass

class CSVFile():
    def __init__(self, name): 
        self.name = name
        if not type(name)==str:
            raise TypeError('il nome del file deve essere una stringa')
        try:
            with open(name, 'r') as file:
                file.readline()
        except FileNotFoundError as e:
            print(f'da __init__() file non trovato, ho avuto un {type(e)}')
    
    def get_data(self, start=None, end=None):
        list = []
        
        with open(self.name, 'r') as file:
            file_lenght = 0
            for line in file:
                file_lenght+=1
                list.append(line.strip())
            
            if start == None:
                    start = 1
            start -= 1
            if end == None: 
                end = file_lenght
            if start<0:
                raise ParameterError('il parametro start non può essere minore di 1!')
            if start>end:
                raise ParameterError('il parametro end non può essere minore di start')
            if end>file_lenght:
                raise ParameterError(f'il file contiene {file_lenght} righe, non posso leggere fino alla {end}')
            
            print(list[start:end])
            return list[start:end]
        

# csv = CSVFile('shampoo.csv')
# csv.get_data(1,5)


class NumericalCSVFile(CSVFile):

    def __init__(self, name):
        super().__init__(name)
    
    def get_data(self):
        sales = []
        with open(self.name, 'r') as file:
            next(file)
            for line in file:
                for index, element in enumerate(line.strip().split(',')):
                    if (index==0):
                        continue
                    sales.append(element)
            for element in sales:
                try:    
                    float (element)
                except ValueError as e:
                    print(f'non puoi convertire una in float! {type(e)}')


                #con il costrutto try-except trovo l'errore e lo bypasso; se voglio bloccare l'esecuzione uso raise

                # if type(element)==str:
                #     raise ValueError ('non puoi convertire una stringa!')
                # else:
                #     float(element)
                #     print(element)

# csv2 = NumericalCSVFile('shampoo.csv')
# csv2.get_data()


class Canguro():

    def __init__(self, contenuto_tasca=None): 
        if contenuto_tasca is None:
            self.contenuto_tasca=[]
        else:
            self.contenuto_tasca = contenuto_tasca      #altrimenti, la lista è come se diventasse una variabile di classe non solo dell'oggetto!

    def intasca(self, oggetto):
        (self.contenuto_tasca).append(oggetto)

    def __str__(self):
        return f'canguro che ha intascato {self.contenuto_tasca}'
    
# can = Canguro()
# guro = Canguro()

# can.intasca('mela')
# print(can)

# print(guro)

class Persona:
    def __init__(self, ruolo, nome, cognome):
        self.ruolo = ruolo
        self.nome = nome
        self.cognome = cognome

    def saluta(self):
        print('Ciao sono ', self.ruolo + ":", self.nome, self.cognome)


class Studente(Persona):

    # costruttore sotto-classe
    def __init__(self, nome, cognome, corso, corsi_freq):
        super().__init__("Studente UNITS", nome, cognome)
        self.corso = corso
        if corsi_freq is None: #qui non puoi mettere if self.corsi_freq, perchè non esiste ancora come varibile! sono ancora nel costruttore!
            self.corsi_freq = []
        else:
            self.corsi_freq = corsi_freq

    # ridefinizione del metodo saluta
    def saluta(self):
        Persona.saluta(self)  # uso esplicito metodo della classe Persona
        print(f"Frequento i corsi: {self.corsi_freq}")


class Docente(Persona):
    def __init__(self, nome, cognome, corso, corsi_ins):
        super().__init__("Docente UNITS", nome, cognome)
        self.corso = corso
        if corsi_ins is None:
            self.corsi_ins = []
        else:
            self.corsi_ins = corsi_ins


    def saluta(self):
        Persona.saluta(self)
        print(f"Insegno i corsi: {self.corsi_ins}")

# marghe = Studente('marghe', 'gio', 'iada', 'analisi, geometria, algebra, programmazione')
# nenzi = Docente('laura', 'nenzi', 'iada', 'programmazione, analisi dati')
# marghe.saluta()
# nenzi.saluta()

from datetime import datetime

def birthday_countdown(birth_day, birth_month):

    ora_esatta = datetime.now()

    data_lista = [ora_esatta.year, ora_esatta.month, ora_esatta.day]
    orario_lista = [ora_esatta.hour, ora_esatta.minute, ora_esatta.second]

    months_dict = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
    # print(data_lista)

    if birth_day==data_lista[2] and birth_month==data_lista[1]:
        print('tanti auguri!')
        return

    days_missing = birth_day + months_dict[data_lista[1]] - data_lista[2] + 1

    hours_missing = 24 - orario_lista[0] + 1

    minutes_missing = 60 - orario_lista[1] + 1
    if minutes_missing>60:
        hours_missing+=1

    seconds_missing = 60 - orario_lista[2]
    if seconds_missing>60:
        minutes_missing+=1

    if birth_month>data_lista[1] or (birth_month>data_lista[1] and birth_day<data_lista[2]):

        full_months_missing = birth_month - data_lista[1] - 1

    else:
        full_months_missing = 12 - data_lista[1] + birth_month + 1 

    print(f'mancano {full_months_missing} mesi, {days_missing} giorni, {hours_missing} ore, {minutes_missing} minuti e {seconds_missing} secondi al tuo compleanno!')

# birthday_countdown(24,2)

def funzione(n=None):

    n = input('insersci un numero intero\n') #il cast a intero funziona solo se il numero in input è una stringa che rappresenta un intero! è super easy!!
    
    while not type(n)==int:
        try:
            n = int(n)
            quadrato = n*n
        except ValueError:
            print('impossibile elevare al quadrato, valore inserito errato')
            n = input('inserisci un nuovo numero valido\n')

    print(quadrato)
    return quadrato

# funzione()

def es_7(option = None):
    print(' 1: calcola somma di due numeri\n 2: calcola la differenza tra due numeri\n 3: uscire')
    option = input('choose an option\n')
    option=option.strip()
    a=0
    b=0
    while not option in ['1','2','3']:
        print('il numero deve essere tra [1,2,3]')
        option = input('inserisci un numero valido')
    
    if option in ['1','2']:
        a = input('inserisci il primo numero\n')
        a = a.strip()
        b = input('inserisci il secondo numero\n')
        b = b.strip()
    if option==3:
        return None
    
    while(not type(a)==float and not type(b)==float):
        try:
            a = float(a)
        except ValueError:
            a = input('inserisci un nuovo numero validoi, quello precedente causa ValuError')
        try:
            b = float(b)
        except ValueError:
            b = input('inserisci un nuovo numero validoi, quello precedente causa ValuError')
    
    if int(option)==1: print(a+b); return a+b
    if int(option)==2: print(a-b); return(a-b)

# es_7()

# lista = [n for n in range(1,6)]
# print(lista)

#iteratori
class Series():

    def __init__(self, low, high):
        self.current = low
        self.high=high

    def __iter__(self):
        return self #ho già settato current nel costruttore, iter deve solo ritornare se stesso
    
    def __next__(self):
        if self.current>self.high:
            raise StopIteration
        else: 
            self.current += 1
            return self.current - 1

# my_list = Series(1,10)
# print(list(my_list)) #se non gli passo list(...) lui mi stampa il puntatore agli oggetti della lista!!!
# #con list comprehension
# my_list2=[]
# [my_list2.append(s) for s in Series(1,10)]
# print(my_list2)

# dispari=[n for n in range(0,9) if n%2==1]
# print(dispari)

# lista_input = [[1,2,3], [4,5],[6,7,8,1]]
# lista_return = []
# [lista_return.append(element) for sublist in lista_input for element in sublist]
# print(lista_return)

# list1 = [1,3,5,7]; list2 = [2,4,6]
# my_list = [elem1*elem2 for elem1 in list1 for elem2 in list2 if elem1*elem2>10]
# print(my_list)

# lista_return = [(a,b,c) for a in range(1,21) for b in range(a,21) for c in range(b,21) if a**2+b**2==c**2] #non serve fare .append()!!!!!
# print(lista_return)

# lista_numeri = [0,1,2,4]
# lista_lettere = ['a','b','c']
# lst = [(numero, lettera) for numero in lista_numeri for index, lettera in enumerate(lista_lettere) if numero%2==0 and index%2==1]
# print(lst)

#dict comprehension

# sentence = 'the cat sat on the mat the cat'
# my_dict = {word:sentence.count(word) for word in sentence.split(' ')}
# print(my_dict)  

air = ["gemini", "libra", "acquarius"]
x = input("insert your zodiac sign:\n")

# if x in air:
#     print(f'{x} is an air sign')
# else:
#     print(f'{x} is not an air sign')

#oppure
# if x in air:
#     print('{} is an air sign'.format(x))
# else:
#     print('{} is not an air sign'.format(x))
