class ExamException(Exception):
    pass

class MovingAverage():

    def __init__(self, widow_lenght):
        self.widow_lenght = widow_lenght
        self.lista_out = []
        if widow_lenght<=0 or not type(widow_lenght)==int:
            raise ExamException('Errore, la lunghezza della finestra deve essere un numero intero strettamente positivo')


    def __str__(self):
        return f'la media mobile di intervallo {self.widow_lenght} è {self.lista_out}'
    
    def compute(self, lista_in):
        self.lista_in = lista_in

        if not type(self.lista_in)==list: raise ExamException('la lista in input deve essere di tipo list')

        for index, element in enumerate(self.lista_in):
            if not type(element)==int: raise ExamException(f'elemento {element} di indice {index} della lista non è un intero; la lista deve contenere solo interi')
            
        if self.widow_lenght>len(lista_in): raise ExamException('la lunghezza della finestra non può superare quella della lista')

        for i in range(len(self.lista_in)-self.widow_lenght+1):
            sum = 0
            for element in self.lista_in[i:i+self.widow_lenght]:
                sum += element
            self.lista_out.append(sum/self.widow_lenght)
        print(self.lista_out)
        return self.lista_out

lista = MovingAverage(4)
lista.compute([2,4,8,16])


    
