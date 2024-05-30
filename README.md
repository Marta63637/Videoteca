Installare Flask
Con l'ambiente virtuale attivato, installa Flask usando pip:

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

Assicurati di essere nella directory del progetto ed esegui il comando:
 ```
python app.py
 ```
Dovresti vedere un output simile a questo:

 ```
* Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 ```

Apri un browser web e naviga a http://127.0.0.1:5000/. Dovresti vedere la pagina con il messaggio "Hello, World!" come in foto 




