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