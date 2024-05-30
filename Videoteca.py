from typing import Any
from FilmC import FilmC

class Videoteca: 
    def __init__(self):
        self.__film = []

    def aggiungi_film(self,film: FilmC):
        if (film.getDisponibilità() == False):
            self.__film.append(film)
            film.setDisponibilità(True)
    
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
        disp = [film.getInfoFilm() for film in self.__film if film.getDisponibilità()]
        if disp:
            print("Film disponibili:")
            for inform in disp:
                print(inform)
        else:
            print("Nessun film disponibile al momento.")



film1 = FilmC("Ciao", "Marta", 2000, False)
film2 = FilmC("Ciao2", "Marta2", 2002, False)
film3 = FilmC("Ciao3", "Marta2", 2002, False)

videoteca = Videoteca()
videoteca.aggiungi_film(film1)
videoteca.aggiungi_film(film2)
videoteca.aggiungi_film(film3)

videoteca.Prestito_film("Ciao3")
videoteca.Restituisci_film("Ciao3")

videoteca.rimuovi_film("Ciao2")
videoteca.cerca_film("Ciao3")
videoteca.getInfoVideoteca()


    
