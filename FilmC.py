class FilmC:
    def __init__(self, titolo:str, regista:str, anno_uscita:int, disponibile:bool):
        self.__titolo=titolo
        self.__regista=regista
        self.__anno_uscita=anno_uscita
        self.__disponibile=disponibile

    def getTitolo(self):
        return self.__titolo
    
    def getRegista(self):
        return self.__regista
    
    def getAnnoUscita(self):
        return self.___anno_uscita
    
    def getDisponibilità(self):
        return self.__disponibile
    
    def setDisponibilità(self, nuova_disponibilità: bool):
        self.__disponibile= nuova_disponibilità

    def getInfoFilm(self):
        return f"Titolo: {self.__titolo},\nRegista: {self.__regista},\nAnno di uscita: {self.__anno_uscita},\nDisponibile: {self.__disponibile}"
    
