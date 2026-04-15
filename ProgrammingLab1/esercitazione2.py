class ExamException(Exception):
    pass

class CSVTimeSeriesFile():
    def __init__(self, name):
        self.name = name
    
    def get_data(self):
        lista_out = []
        try:
            with open(self.name, 'r') as file:
                next(file)
                for line in file:
                    lista_out.append(line.strip().split(','))
            
            for elem in lista_out: #converto i valori a intero
                if elem[1]!='':
                    elem[1]=int(elem[1])
            
            lista_clean = [x for x in lista_out if x[1]!= ''] #pulisco la lista dai missing values
            
            return lista_clean
        except FileNotFoundError:
            raise ExamException('file non trovato')
    

def compute_variations(time_series, first_year, last_year):
    dict_years={}
    for elem in time_series:
        anno = elem[0]
        anno = anno[0:4]
        valore = elem[1]

        if anno not in dict_years:
            dict_years[anno]=[]
        
        dict_years[anno].append(valore)
    
    dict_media_anno = {}
    for anno in dict_years.keys():
        somma = sum(dict_years[anno])
        media = somma/len(dict_years[anno])
        dict_media_anno[anno]=media

    indice = first_year
    dict_return={}
    while not(indice)==last_year:
        anno = int(indice)
        successivo=anno+1
        if str(indice) in dict_media_anno and str(successivo) in dict_media_anno:
            curr_average = dict_media_anno[str(anno)]
            next_average = dict_media_anno[str(successivo)]
            dict_return[f'{anno}-{successivo}']=next_average-curr_average
        indice+=1
    
    print(dict_return)
    return(dict_return)





    
time_series_file = CSVTimeSeriesFile('data.csv')
time_series = time_series_file.get_data() 
# print(time_series_file.get_data())
compute_variations(time_series, 1949,1956)
