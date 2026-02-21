from flask import Flask
import random

app = Flask(__name__)

@app.route("/")
def hello_world():
    return '<h1>Hello, World!</h1> <br> <a href="/palavras">Veja uma palavra aleatório!</a> <br> <a href="/Charada">Veja uma charada!</a> '

@app.route("/palavras")
def palavras():
    words = [
        "Diáfano = Transparente, claro, límpido.",
        "Efêmero = Que dura pouco tempo, passageiro.",
        "Alinhavo: Esboço, rascunho, ou alinhavo de costura.",
        "Lesto: Rápido, ágil, ligeiro.",
        "Incólume: Intacto, são e salvo, que não sofreu danos."
    ]
    return f'<p>{random.choice(words)}</p> <br> <p>Reinicie a página para ver mais palavras aleatórias!</p> <br> <a href="/">Volte para o início!</a> '

@app.route("/SONIC")
def SONIC():
    return '<h1>Sonic é o ouriço mais rápido!</h1>'

@app.route("/Charada")
def Charada():
    return '<h1>O que é, o que é? Sobe, sobe, sobe e jamais desce.</h1> <br> <a href="/RespostaCharada">Veja a resposta da charada!</a> '

@app.route("/RespostaCharada")
def RespostaCharada():
    return '<h1>A idade.</h1> <br> <a href="/Charada">Volte para a charada!</a> <br> <a href="/">Volte para o início!</a> '


app.run(debug=True)
