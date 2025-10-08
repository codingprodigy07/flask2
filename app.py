from flask import Flask, render_template
import random

app = Flask(__name__)

imena = ["Luka", "Maja", "Nik", "Eva", "Mark", "Tina", "Jure", "Sara", "Klara", "Tomi"]
priimki = ["Novak", "Horvat", "Kovačić", "Zupan", "Potočnik", "Jovanović", "Babić", "Kralj", "Vidmar", "Zajc"]
starosti = [25, 32, 28, 24, 30, 27, 33, 29, 26, 31]
kraji_rojstva = ["Ljubljana", "Maribor", "Celje", "Koper", "Novo mesto", "Ptuj", "Velenje", "Izola", "Kranj", "Škofja Loka"]
imena_ulic = ["Cesta v mestni log", "Glavna ulica", "Trg svobode", "Parkovna pot", "Mala ulica", "Breg", "Podgrad", "Zgornja ulica", "Dolga cesta", "Ribniška cesta"]



@app.route("/")
def randomOseba():
        ime = random.choice(imena)
        priimek = random.choice(priimki)
        starost = random.choice(starosti)
        kraj_rojstva =  random.choice(kraji_rojstva)
        ime_ulice = random.choice(imena_ulic)
        številka_ulice = random.randint(1,100)
        return render_template("Index.html", naslov="Naključna oseba", ime = ime, priimek = priimek, starost = starost, kraj_rojstva = kraj_rojstva, ime_ulice = ime_ulice, številka_ulice = številka_ulice)

if __name__ == "__main__":
    app.run(debug=True)
