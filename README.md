Installare Flask
installa Flask usando pip, all'interno del cmd:

 ```
pip install Flask
 ```
Crea una nuova directory per il tuo progetto, se non lo hai già fatto.
All'interno della directory del progetto, crea un file chiamato app.py con il seguente contenuto:

 ```
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(debug=True)
 ```
Per essere specifici e permettere una comprensione completa: 
 ```
from flask import Flask
 ```
Questo comando importa la classe Flask dal pacchetto Flask. Flask è la classe principale del framework Flask e viene utilizzata per creare l'applicazione.
 ```
app = Flask(__name__)
 ```
Qui creiamo un'istanza dell'applicazione Flask. Il parametro __name__ è una variabile predefinita di Python che rappresenta il nome del modulo attuale. Viene passato all'istanza Flask per aiutare l'applicazione a configurarsi correttamente, specialmente per la gestione dei percorsi dei file e delle risorse. 

 ```
@app.route('/')
 ```
Questo è un decorator di Flask che associa una funzione a un particolare URL. In questo caso, @app.route('/') significa che la funzione sottostante sarà chiamata quando un utente visita l'URL radice (/) dell'applicazione (nel nostro caso il localhost 127.0.0.1:5000).

 ```
def hello_world():
    return 'Hello, World!'
 ```
Questa è la funzione che viene eseguita quando l'URL radice (/) viene richiesto (quando vi si clicca sopra). La funzione restituisce la stringa 'Hello, World!', che sarà inviata come risposta al browser web.

 ```
if __name__ == '__main__':
    app.run(debug=True)
 ```
Questo blocco condizionale verifica se lo script è eseguito direttamente (e non importato come modulo). Se la condizione è vera, l'applicazione Flask viene avviata. app.run(debug=True) avvia il server web di Flask. debug=True: Questo parametro attiva il debug mode. In modalità debug, l'applicazione si aggiorna automaticamente ogni volta che si modificano i file di codice e mostra informazioni di debug in caso di errori. È utile durante lo sviluppo, ma dovrebbe essere disattivato in produzione per motivi di sicurezza.

Assicurati di essere nella directory del progetto ed esegui il comando:
 ```
python app.py
 ```
Dovresti vedere un output simile a questo:

 ```
* Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 ```
Apri un browser web e naviga a http://127.0.0.1:5000/. Dovresti vedere la pagina con il messaggio "Hello, World!" come in foto.
A questo punto si voleva unire il lavoro svolto in precedenza sulle classi Videoteca.py e FilmC.py per renderlo direttamente modificabile dall'utente nella pagina web.
Si riscrivono per chiarezza subito sotto

 ```
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
 
 ```
**CLASSE COMPOSTA DA UN COLLEZIONE DI FILM --> VIDEOTECA**
 
 ```
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
 ```
Per fare ciò si è creata una pagina HTML chiamata home.html
 ```
<!DOCTYPE html>
<html>
<head>
    <title>My Flask App</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
        }
        h1 {
            color: #333;
            margin-bottom: 10px;
        }
        table {
            border-collapse: collapse;
            width: 100%;
        }
        th, td {
            border: 1px solid #ddd;
            padding: 10px;
            text-align: left;
        }
        th {
            background-color: #f2f2f2;
        }
        form {
            margin-bottom: 20px;
        }
        label {
            display: block;
            margin-bottom: 5px;
        }
        input[type="submit"] {
            background-color: #A020F0;
            color: #fff;
            padding: 10px 20px;
            border: none;
            cursor: pointer;
        }
        input[type="submit"]:hover {
            background-color: #A020F0
        }
        input[type="text"], input[type="checkbox"] {
            width: 100%;
            padding: 10px;
            margin-bottom: 10px;
            border: 1px solid #ccc;
            max-width: 80%;
        }
    </style>
</head>
<body>
    <h1>Benvenuto nella mia Videoteca</h1>
    <table>
        <tr>
            <td>
                <h1>Aggiungi un film</h1>
                <form method="POST" action="/form1">
                    <label for="titolo">Inserisci il titolo del film:</label>
                    <input type="text" id="titolo" name="titolo" value="{{ titolo }}">
                    <label for="regista">Regista:</label>
                    <input type="text" id="regista" name="regista" value="{{ regista }}">
                    <label for="anno">Inserisci l'anno:</label>
                    <input type="text" id="anno" name="anno" value="{{ anno }}">
                    <input type="checkbox" name="bool" value="True">
                    <input type="submit" value="Invia">
                </form>
            </td>
            <td>
                <h1>Ricerca un film</h1>
                <form method="POST" action="/form2">
                    <label for="ricerca">Inserisci il titolo del film che vuoi ricercare:</label>
                    <input type="text" id="ricerca" name="ricerca" value="{{ ricerca }}">
                    <input type="submit" value="Invia">
                </form>
            </td>
        </tr>
        <tr>
            <td>
                <h1>Rimuovi film</h1>
                <form method="POST" action="/form3">
                    <label for="rimuovi">Inserisci il titolo del film che vuoi rimuovere:</label>
                    <input type="text" id="rimuovi" name="rimuovi" value="{{ rimuovi }}">
                    <input type="submit" value="Invia">
                </form>
            </td>
            <td>
                <h1>Prendi in prestito un film</h1>
                <form method="POST" action="/form4">
                    <label for="prestito">Inserisci il titolo del film che vuoi prendere in prestito:</label>
                    <input type="text" id="prestito" name="prestito" value="{{ prestito }}">
                    <input type="submit" value="Invia">
                </form>
            </td>
        </tr>
        <tr>
            <td>
                <h1>Restituisci un film</h1>
                <form method="POST" action="/form5">
                    <label for="restituisci">Inserisci il titolo del film che vuoi restituire:</label>
                    <input type="text" id="restituisci" name="restituisci" value="{{ restituisci }}">
                    <input type="submit" value="Invia">
                </form>
            </td>
        </tr>
    </table>
</body>
</html>
 ```
Per quanto riguarda l'HTML: HTML (HyperText Markup Language) è il linguaggio standard per creare e strutturare pagine web. È un linguaggio di markup che utilizza una serie di elementi e tag per descrivere il contenuto e la struttura di una pagina web. HTML definisce la semantica del contenuto, permettendo ai browser di visualizzarlo correttamente. I Tag HTML sono costrutti che delimitano gli elementi HTML. Un tag tipico è costituito da un nome racchiuso tra parentesi angolari (< e >). Ci sono due tipi principali di tag:
- Tag di apertura: Inizia un elemento HTML. Esempio:
 ```
<p>
 ```
Questo tag di apertura inizia un paragrafo.
- Tag di chiusura: Termina un elemento HTML. È simile al tag di apertura ma preceduto da una barra (/). Esempio:
 ```
</p>
 ```
Questo tag di chiusura termina il paragrafo.
Alcuni tag sono auto-chiudenti e non richiedono un tag di chiusura. Esempio:
 ```
<img src="image.jpg" alt="descrizione">
 ```
Questo tag img inserisce un'immagine.
Per strutturare una pagina HTML si inizia sempre con la dichiarazione del tipo di documento:

 ```
<!DOCTYPE html>
 ```
Indica che il documento è scritto in HTML5 e successivamente viene aperto il tag <html>
 ```
<html>
 ```
AL suo interno contiene tutto il contenuto della pagina web.
Elemento <head>:
 ```
<head>
 ```
Contiene meta-informazioni sulla pagina, inclusi il titolo e gli stili CSS, di cui parleremo subito dopo la descrizione dell'HTML.
 ```
<title> Videoteca </title>
 ```
Definisce il titolo della pagina che appare sulla scheda del browser.
 ```
<style>
 ```
Contiene gli stili CSS per la pagina.
 ```
<body>
 ```
Contiene il contenuto visibile della pagina web. Quello che compare all'interno della pagina e visibili all'utente.
 ```
<h1>Benvenuto nella mia Videoteca</h1>
 ```
Definisce un'intestazione di primo livello (titolo di grandi dimensioni, rispetto ad h2,h3,h4... dove si parla di sottotitoli di dimensioni sempre minori) con il testo "Benvenuto nella mia Videoteca".
 ```
<table>
 ```
Crea una tabella per organizzare i moduli.
 ```
<tr>
 ```
Definisce una riga nella tabella.
 ```
<td>
 ```
Definisce una cella in una riga della tabella.
 ```
<form method="POST" action="/form1">
 ```
Crea un modulo HTML per inviare dati al server tramite il metodo POST all'URL specificato della mia pagina py dove si programma Flask.
 ```
<label for="titolo">Inserisci il titolo del film:</label>
 ```
Associa un'etichetta descrittiva a un controllo di input. E' la scritta affianco alle diverse _textbox_ necessario per comprendere cosa si richiede di inserire
 ```
<input type="text" id="titolo" name="titolo" value="{{ titolo }}">
 ```
Crea un campo di input per l'utente. type="text" specifica un campo di testo, quindi una casella di testo dove è possibile per l'utente scrivere.

 ```
<input type="submit" value="Invia">
 ```
Crea un pulsante di invio per il modulo di tutte le informazioni inserite nella casella di testo corrispondente. E' necessario **per ogni form diverso, un pulsante submit differente**. Spiegazione del CSS:
CSS (Cascading Style Sheets) è un linguaggio utilizzato per descrivere l'aspetto e la formattazione di un documento scritto in HTML. Mentre HTML fornisce la struttura del contenuto della pagina web, CSS gestisce lo stile e il layout, permettendo di separare la presentazione dal contenuto.
Le funzioni Principali del CSS:
- Stilizzare il Contenuto: Cambia l'aspetto di testi, immagini, e altri elementi HTML (es. colore, font, dimensioni).
- Layout: Dispone gli elementi sulla pagina (es. margini, padding, posizionamento).
- Responsive Design: Adatta il layout per diverse dimensioni di schermo e dispositivi.
Il CSS è composto da regole che selezionano gli elementi HTML e specificano come devono essere stilizzati.
Ad esempio il body nel mio codice CSS:
 ```
body {
    font-family: Arial, sans-serif;
    margin: 20px;
}
 ```
Imposta il font del corpo del documento a Arial (o sans-serif se Arial non è disponibile) e un margine di 20px. Quello che può venire scritto all'interno delle parentesi è infinito (vi sono infatti diversi innumerevoli _references_ scritte tutte a questo sito https://www.w3schools.com/cssref/index.php). 
Anche le parti dell'HTML che vengono modificate possono essere innumerevoli, oltre ai nomi dei diversi tag, si possono anche creare classi di tag e id (tutti scritti a questa pagina https://www.w3schools.com/cssref/css_selectors.php) e vengono creati per raggruppare gruppi di diversi tag che devono avere lo stesso identico stile (come ad esempio anche alcuni pulsanti, o alcuni tipi di testi). 

Dopo la creazione del'HTML con i diversi form si è passato alla modifica del flask per creare cinque diverse funzioni in grado di passare le informazioni inserite nell'utente per creare oggetti di FilmC e, di conseguenza, delle Videoteche. 
Per fare ciò la pagina di Flask è stata modificata come segue:
 ```
from flask import Flask, render_template, request
#main class è Flask per creare le web application, render_template funzione che renderizza il templat html

from Videoteca import Videoteca
from FilmC import FilmC

risultato = Videoteca()

app = Flask(__name__) #passa il nome del modulo corrente. Crea una nuova istanza dell'applicazione che useremo
#per definire i routes e per configurarla

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/form1', methods =['GET', 'POST'])

def formLudoteca():
    titolo = None
    regista = None
    if request.method == 'POST':
        titolo = request.form.get('titolo')
        regista = request.form.get('regista')
        anno_uscita = request.form.get('anno')
        disp = request.form.get('bool')

        film = FilmC(titolo,regista, int(anno_uscita), bool(disp))
        risultato.aggiungi_film(film)
        risultato.getInfoVideoteca()

    return render_template('home.html', titolo=titolo, regista=regista)

@app.route('/form2', methods =['GET', 'POST'])
def formLudoteca2():
    titolo = None
    if request.method == 'POST':
        titolo =request.form.get('ricerca')
    risultato.cerca_film(titolo)
    return render_template('home.html', titolo=titolo)

@app.route('/form3', methods =['GET', 'POST'])
def formLudoteca3():
    titolo = None
    if request.method == 'POST':
        titolo =request.form.get('rimuovi')
    risultato.rimuovi_film(titolo)
    return render_template('home.html', titolo=titolo)

@app.route('/form4', methods =['GET', 'POST'])
def formLudoteca4():
    titolo = None
    if request.method == 'POST':
        titolo =request.form.get('prestito')
    risultato.Prestito_film(titolo)
    return render_template('home.html', titolo=titolo)

@app.route('/form5', methods =['GET', 'POST'])
def formLudoteca5():
    titolo = None
    if request.method == 'POST':
        titolo =request.form.get('restituisci')
        risultato.Restituisci_film(titolo)
    return render_template('home.html', titolo=titolo)

if __name__ == '__main__':
#Questa riga è una clausola di guardia che garantisce che il codice seguente venga eseguito solo quando lo script viene eseguito direttamente (ovvero, non quando viene importato come modulo da un altro script).
    app.run(debug=True)
 ```
Analizzando riga per riga:
 ```
def formLudoteca():
 ```
La funzione formLudoteca viene definita senza parametri. Gestisce una richiesta HTTP e si aspetta di essere invocata in risposta a una richiesta a un determinato endpoint. Si inizializzano le variabili:
 ```
titolo = None
regista = None
 ```
Le variabili titolo e regista vengono inizializzate a None. Queste variabili verranno successivamente utilizzate per memorizzare i dati inviati tramite un modulo (form) HTML.
 ```
if request.method == 'POST':
 ```
Qui si controlla se il metodo della richiesta HTTP è POST. Questo indica che il modulo è stato inviato dal client. La differenza con GET è nel fatto che quest'ultimo, invece, consiste nell'accodare all'indirizzo della pagina web (URL) i diversi parametri contenenti i dati che si vogliono trasmettere; all'URL originale viene quindi aggiunto alla fine un punto interrogativo seguito dai parametri e dai dati da trasferire.
 ```
titolo = request.form.get('titolo')
regista = request.form.get('regista')
anno_uscita = request.form.get('anno')
disp = request.form.get('bool')
 ```
Vengono estratti i dati inviati tramite il modulo HTML utilizzando request.form.get(). I campi attesi nel modulo sono titolo, regista, anno e bool (presumibilmente uno stato di disponibilità).
 ```
film = FilmC(titolo, regista, int(anno_uscita), bool(disp))
 ```
Viene creata un'istanza della classe FilmC con i dati appena raccolti. I dati estratti dal modulo vengono utilizzati per inizializzare questa istanza. anno_uscita viene convertito in un intero e disp viene convertito in un booleano per essere sicuri che il passaggio avvenga nel modo corretto per far successivamente funzionare i diversi metodi.
 ```
risultato.aggiungi_film(film)
risultato.getInfoVideoteca()
 ```
L'oggetto film viene aggiunto a un oggetto risultato tramite il metodo aggiungi_film e poi viene stampata a terminale la videoteca.
Questo viene ripetuto cambiando il metodo per gli altri form.


