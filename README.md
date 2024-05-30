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

Andando nello specifico from flask import Flask

Apri un browser web e naviga a http://127.0.0.1:5000/. Dovresti vedere la pagina con il messaggio "Hello, World!" come in foto 




