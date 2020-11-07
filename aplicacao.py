from flask import Flask
from flask import render_template, request, url_for, redirect


app = Flask(__name__)


@app.route("/teste")
def teste():
    return 'Hello, world!'


@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")


@app.route("/internacional")
def internacional():
    return render_template("internacional.html")


@app.route("/flamengo")
def flamengo():
    return render_template("flamengo.html")


@app.route("/atletico_mg")
def atletico_mg():
    return render_template("atletico_mg.html")


@app.route("/fluminense")
def fluminense():
    return render_template("fluminense.html")


@app.route("/sao_paulo")
def sao_paulo():
    return render_template("sao_paulo.html")


@app.route("/santos")
def santos():
    return render_template("santos.html")


@app.route("/palmeiras")
def palmeiras():
    return render_template("palmeiras.html")


@app.route("/gremio")
def gremio():
    return render_template("gremio.html")


@app.route("/sport_recife")
def sport_recife():
    return render_template("sport_recife.html")


@app.route("/fortaleza")
def fortaleza():
    return render_template("fortaleza.html")


@app.route("/corinthians")
def corinthians():
    return render_template("corinthians.html")


@app.route("/ceara_sc")
def ceara_sc():
    return render_template("ceara_sc.html")


@app.route("/atletico_go")
def atletico_go():
    return render_template("atletico_go.html")


@app.route("/botafogo")
def botafogo():
    return render_template("botafogo.html")


@app.route("/bahia")
def bahia():
    return render_template("bahia.html")


@app.route("/vasco_da_gama")
def vasco_da_gama():
    return render_template("vasco_da_gama.html")


@app.route("/coritiba")
def coritiba():
    return render_template("coritiba.html")


@app.route("/bragantino_sp")
def bragantino_sp():
    return render_template("bragantino_sp.html")


@app.route("/athletico_pr")
def athletico_pr():
    return render_template("athletico_pr.html")


@app.route("/goias")
def goias():
    return render_template("goias.html")


if __name__ == "__main__":
    app.run(debug=True)
