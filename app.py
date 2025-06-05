from flask import Flask, render_template_string, request

app = Flask(__name__)

HTML_TEMPLATE = """
<!doctype html>
<html lang=\"is\">
  <head>
    <meta charset=\"utf-8\">
    <title>Reikna regnvatn</title>
    <style>
      body {
        font-family: Arial, sans-serif;
        background-color: #f2f9fb;
        color: #003846;
        text-align: center;
        padding: 2em;
      }
      h1 {
        color: #006e85;
      }
      form {
        background: #ffffff;
        border-radius: 8px;
        padding: 2em;
        display: inline-block;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
      }
      input, button {
        padding: 0.6em;
        margin-top: 1em;
        font-size: 1em;
        border-radius: 4px;
        border: 1px solid #ccc;
      }
      button {
        background-color: #009ca6;
        color: white;
        border: none;
        cursor: pointer;
      }
      button:hover {
        background-color: #007a85;
      }
      .results {
        margin-top: 2em;
        background-color: #e7f5f8;
        padding: 1em;
        border-radius: 8px;
        display: inline-block;
      }
      .info-boxes {
        margin-top: 2em;
        display: flex;
        flex-wrap: wrap;
        justify-content: center;
        gap: 1em;
      }
      .info-box {
        background-color: #ffffff;
        border: 1px solid #009ca6;
        border-radius: 8px;
        padding: 1em;
        width: 400px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
      }
      .info-box h3 {
        color: #006e85;
        margin-bottom: 0.5em;
      }
      .images {
        margin-top: 2em;
        display: flex;
        flex-wrap: wrap;
        justify-content: center;
        gap: 2em;
      }
      .images img {
        width: 300px;
        border-radius: 10px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.15);
      }
      .logo {
        width: 120px;
        margin-bottom: 1em;
      }
    </style>
  </head>
  <body>
    <img src=\"/static/veitur_logo.png\" alt=\"Veitur logo\" class=\"logo\">
    <h1>Mér finnst rigningin góð</h1>
    <h1>Reiknivél fyrir regnvatn</h1>
    <form method=\"post\">
      <label>Sláðu inn flatarmál lóðarinnar (í m²):</label><br>
      <input type=\"number\" name=\"area\" step=\"0.01\" required>
      <br>
      <button type=\"submit\">Reikna</button>
    </form>

    {% if result is not none %}
    <div class=\"results\">
      <h2>Niðurstöður</h2>
      <p>Magn regnvatns: {{ result }} lítrar á ári.</p>
      <p>Fjöldi baðkara: {{ bathtubs }}.</p>
    </div>

    <div class=\"info-boxes\">
      <div class=\"info-box\">
        <h3>Regngarður</h3>
        <p>Regngarðar eru bæði falleg og hagnýt lausn sem stuðlar að minni ofanvatnsrennsli, bættri vatnsgæðum og auknu lífríki í nærumhverfinu.

</p>
      </div>
      <div class=\"info-box\">
        <h3>Regntunna</h3>
        <p>Regnvatnstunnur safna vatni af þökum sem annars færi beint í niðurföll. Vatnið má síðan nýta til vökvunar garða eða annarra nota og þannig spara hreint vatn og létta á fráveitu.</p>
      </div>
    </div>

    <div class=\"info-boxes\">
      <div class=\"info-box\">
        <h3>Gegndræp efni</h3>
        <p>Með því að nota gegndræp yfirborðsefni í innkeyrslur og gönguleiðir – eins og grashellur, möl eða gegndræpa steypu – getur regnvatn síast niður í jarðveginn í stað þess að renna yfir malbik og beint í niðurföll. Þetta dregur úr flóðahættu, bætir grunnvatnsstöðu og dregur úr mengun sem annars færi með yfirborðsvatni í sjó og vötn.</p>
      </div>
      <div class=\"info-box\">
        <h3>Græn þök</h3>
        <p>Græn þök eru þök sem eru klædd gróðri og jarðvegi sem tekur við úrkomu, hægir á rennsli og veitir einangrun. Þau bæta einnig loftgæði og stuðla að líffræðilegum fjölbreytileika.</p>
      </div>
    </div>

    <div class=\"images\">
      <img src=\"/static/page1.jpg\" alt=\"Rain Gardens\">
      <img src=\"/static/page2.jpg\" alt=\"Permeable Driveways and Patios\">
      <img src=\"/static/page3.jpg\" alt=\"Blue Green Roofs\">
    </div>
    {% endif %}
  </body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    bathtubs = None
    if request.method == "POST":
        try:
            area = float(request.form["area"])
            result = round(area * 0.8 * 1000)
            bathtubs = round(result / 150)
        except ValueError:
            result = None
    return render_template_string(HTML_TEMPLATE, result=result, bathtubs=bathtubs)

import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

