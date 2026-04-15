class ExamException(Exception):
    pass

class CSVTimeSeriesFile():

    def __init__(self, name):
        self.name = name
        try:
            with open(name, 'r') as file:
                file.read()
        except FileNotFoundError:
            raise ExamException('Il file non esiste')
    
    def get_data(self):

        with open(self.name, 'r') as file:
            next(file)
            lista_return = []
            for line in file:
                lista_return.append(line.strip().split(','))
            
            for index, elem in enumerate(lista_return):
                try:
                    elem[1] = float(elem[1])
                except TypeError:
                    print(f'la riga corrispondente a {elem[0]} contiene un valore non numerico {elem[1]}, pertanto verrà ignorata')
                except ValueError:
                    print(f'la riga corrispondente a {elem[0]} contiene un valore non numerico {elem[1]}, pertanto verrà ignorata')

        lista_return= [x for x in lista_return if type(x[1])==float]
        
        return(lista_return)

def compute_variations(time_series, first_year, last_year, N):
    """
    Questa funzione calcola:
    - dict_anno : un dizionario che ha come chiave l'anno e come valori una lista con tutte le medie mensili raggruppate per anno
    - dict_media: un dizionario che ha come chiave l'anno e come valore la media annuale delle variazioni
    """
    # creazione di dict_anno come spiegato
    if(N>=last_year-first_year): raise ExamException('la finestra N deve essere strettamente minore dell intervallo considerato')
    dict_anno = {}
    for element in time_series:
        anno = element[0]
        anno = anno[0:4]
        valore = element[1]

        if anno not in dict_anno:
            dict_anno[anno]=[]
        
        dict_anno[anno].append(valore)

    # creazione di dict_media 
    dict_media = {}
    for element in dict_anno:
        media = sum(dict_anno[element])/len(dict_anno[element])
        dict_media[element]=media

    def moving_average(dict_media, N, anno):
        somma = 0
        count=0
        anno = int(anno)
        anno_inizio = anno-N
        anno_fine = anno-1
        chiavi = list(dict_media.keys())
        if anno-N>=1900:
            while(anno_inizio<=anno_fine):
                if str(anno_inizio) not in chiavi: 
                    first_year+=1
                    continue
                somma += dict_media[str(anno_inizio)]
                count+=1
                anno_inizio+=1
            media = somma/count
        else: 
            raise ExamException('il primo anno da considerare è il 1900')
        return media

    dict_return = {}
    chiavi = list(dict_media.keys())
    for anno in chiavi:
        anno = int(anno)
    if first_year-N<1900: first_year = 1900+N
    while(first_year<=last_year):
        dict_return[str(first_year)]=dict_media[str(first_year)]-moving_average(dict_media, N, first_year)
        first_year+=1

    return(dict_return)
    
    
time_series_file = CSVTimeSeriesFile('GlobalTemperatures.csv')
time_series = time_series_file.get_data()
print(compute_variations(time_series, 1900, 2000, 10))



    
    




