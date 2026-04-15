#lez06_es1

# class CSVFile:

#     def __init__(self, name):
#         self.name = name

#     def get_data(self):
#         try:    
#             with open ("shampoo.csv", "r") as file:
#                 lista = []
# #               righe = file.readlines()  # legge tutto il file e mette le righe in una lista
#                 for righe in file:
#                     lista.append(righe.strip().split(',')) # strip: rimuove spazi, split: mette la virgola
#                 return lista
#         except FileNotFoundError:
#             print("Errore: il file non esiste!")



# class CSVFile:

#     def __init__(self, name):
#         self.name = name
#         try:
#             with open(self.name, 'r') as file:
#                 file.readline()
#         except FileNotFoundError:
#             print('file non trovato')

#     def get_data(self):
#         try:    
#             with open ("shampoo.csv", "r") as file:
#                 lista = []
# #               righe = file.readlines()  # legge tutto il file e mette le righe in una lista
#                 for righe in file:
#                     lista.append(righe.strip().split(',')) # strip: rimuove spazi, split: mette la virgola
#                 return lista
#         except FileNotFoundError:
#             print("Errore: il file non esiste!")

# file = CSVFile('shampoo.csv')
# print(file.get_data())

#lez06_es4

class CSVFile:

    def __init__(self, name):
        self.name = name
        try:
            with open(self.name, 'r') as file:
                file.readline()
        except FileNotFoundError:
            print('file non trovato')
        
        if not isinstance(name, str):
            raise TypeError ('il nome deve essere una str')

    def get_data(self, start = None, end = None):
        if start == None: start = 1
        if end == None: end = 6
        try:    
            with open ("shampoo.csv", "r") as file:
                lista = [] 
                i=0
                for righe in file:
                    if start <= i & i<=end:
                        lista.append(righe.strip().split(',')) # strip: rimuove spazi, split: mette la virgola
                        i+=1
                    else: i+=1
                return lista 
        except FileNotFoundError:
            print("Errore: il file non esiste!")

file = CSVFile('shampoo.csv')
print(file.get_data())


