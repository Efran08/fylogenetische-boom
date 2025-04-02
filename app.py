"""
In deze python script zorgen wij ervoor dat we via een app.route naar onze website worden gestuurd.
met verschillende argumenten die we geven in de app.route zorgen wij ervoor dat er een
overzichtelijke route is voor de website.
Efran Huliseln, Herke Wilts, Alana Hummel, Gea Bakker en Wytze Meijer.
versie 1.3
21-03-25
"""

import os
from flask import Flask, render_template, request
from fasttree import FastTree


app = Flask(__name__)
UPLOAD_FOLDER = 'fylogenetische-boom/Uploads'
ALLOWED_EXTENSIONS = {'fasta', 'phylip', 'fa', 'phy'}

@app.route('/')
def home_pagina():
    """
    Als we dit script runnen komt deze pagina te voor schijn
    :return: Je krijgt als return de home_page.html, wat ons home pagina is van onze website.
    """
    return render_template('home_page.html')

@app.route('/about')
def dynamische_about_pagina():
    """
    achtergrond informatie staat er over de tools in de About_pagina.html
    :return: als je in de adresbalk /about intypt krijg je de About_pagina.html
    """
    return render_template('About_page.html')

@app.route('/tutorial')
def tutorial_pagina():
    """
    achtergrond informatie staat er over het installeren van de tools in de tutorial_page.html
    :return: als je in de adresbalk /tutorial intypt krijg je de tutorial_page.html
    """
    return render_template('tutorial_page.html')

@app.route('/tool', methods=['GET', 'POST'])
def tool_gebruiken():
    """
    Hier vul je een Fasta of PHILYP bestand in.
    :return: een fylogenetische-boom
    """
    if request.method == 'GET':
        # defalt response when a form is called. Renders 'form/form_file_upload.html'
        return render_template('tool_gebruiken_page.html')

    if request.method == 'POST':
        # response when the submit button is clicked in the 'form/form_file_upload.html'
        # get file from request object
        
        f = request.files['file']

        file_path = os.path.join(
            UPLOAD_FOLDER, f.filename)

        f.save(file_path)

        fasttree = FastTree(file_path)
        fasttree.run_fasttree()

        tree_output = "hier komt later een fylogenetische boom"

        return render_template('tool_output.html', tree=tree_output)

@app.route('/contact', methods=['GET', 'POST'])
def contact_pagina():
    """
    Hierin wordt er een get en post functie gemaakt, waarin er vanuit de website een connectie
    naar deze flask functie word gestuurd. Deze functie moet ervoor zorgen dat er een
    nieuwe pagina wordt weergegeven met de input van de gebruiker die is gestuurd.
    :return:
    """
    if request.method == 'GET': #
        return render_template('contact_page.html')
    if request.method == 'POST':
      kwargs = {
          'name' : request.form['name'],
          'email' : request.form['email'],
          'message' : request.form['message']
      }
    return render_template('contact_us_output.html', **kwargs)

if __name__ == '__main__':
    app.run(debug=True)
