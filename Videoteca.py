from typing import Any
from FilmC import FilmC

class Videoteca: 
    def __init__(self):
        self.__film = []

    def aggiungi_film(self,film: FilmC):
        if (film.getDisponibilità() == False):
            self.__film.append(film)
            film.setDisponibilità(True)
            print (self.__film)
        else:
            ("Il film è già presente in catalogo")
    
    def rimuovi_film(self,titolo: FilmC):
        for i in self.__film:
            if i.getTitolo() == titolo:
                i.setDisponibilità(False)
                print ("Hai rimosso il film", titolo)

    def cerca_film(self,titolo:str):
        for i in self.__film:
            if i.getTitolo() == titolo:
                print ("Ecco il tuo film!", titolo)
    
    def Prestito_film(self, titolo: str):
        for i in self.__film:
            if i.getTitolo() == titolo and i.getDisponibilità():
                i.setDisponibilità(False)
                print(f"Il film {titolo} è stato noleggiato.")
                return
            else:
                print(f"Il film {titolo} non è disponibile per il noleggio.")
        return print(f"Il film {titolo} non è stato trovato. Riprova.")

    def Restituisci_film(self, titolo: str):
        for i in self.__film:
            if i.getTitolo() == titolo:
                i.setDisponibilità(True)
                print(f"Il film {titolo} è stato restituito.")
                return
        return print("Il film non risulta in prestito")
   
    def getInfoVideoteca(self):
        #disp = [film.getInfoFilm() for film in self.__film if film.getDisponibilità()]
        result = []
        for film in self.__film:
            dispo = film.getDisponibilità()
            if dispo:
                info_film = film.getInfoFilm()
                result.append(info_film)
        if dispo:
            print("Film disponibili:")
            for inform in result:
                print(inform)
        else:
            print("Nessun film disponibile al momento.")






    
