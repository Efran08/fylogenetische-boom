"""
In deze python script zorgen wij ervoor dat we via een app.route naar onze website worden gestuurd.
met verschillende argumenten die we geven in de app.route zorgen wij ervoor dat er een
overzichtelijke route is voor de website.
Efran Huliseln, Herke Wilts, Alana Hummel, Gea Bakker en Wytze Meijer.
versie 1.3
21-03-25
"""
import os
import pstats
import cProfile
from functools import wraps
from flask import Flask, render_template, request, url_for
from fasttree import FastTree

app = Flask(__name__)
UPLOAD_FOLDER = os.path.join(app.root_path, 'uploads')
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
ALLOWED_EXTENSIONS = {'fasta', 'phylip', 'fa', 'phy'}


def profile_route(func):
    """
    Decorator die de uitvoering van een routefunctie profileert met cProfile.
    Het resultaat wordt opgeslagen in een .prof-bestand en weergegeven in de console.
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        # Start profiling
        profiler = cProfile.Profile()
        profiler.enable()

        # Voer de originele functie uit en bewaar het resultaat
        result = func(*args, **kwargs)

        # Stop profiling
        profiler.disable()

        # Bestand waarin profilingdata wordt opgeslagen
        profile_files = 'profile_output.prof'
        profiler.dump_stats(profile_files)

        # Laad en sorteer de statistieken op cumulatieve tijd
        stats = pstats.Stats(profile_files)
        stats.sort_stats('cumtime')
        stats.print_stats()  # Zorg dat de stats ook daadwerkelijk worden getoond

        # Print ter bevestiging dat profilingdata is weggeschreven
        print(f'Profiling opgeslagen in: {profile_files}')

        return result

    return wrapper


@app.route('/')
@profile_route
def home_pagina():
    """
    Als we dit script runnen komt deze pagina te voor schijn
    :return: Je krijgt als return de home_page.html, wat ons home pagina is van onze website.
    """
    return render_template('home_page.html')

@app.route('/about')
@profile_route
def dynamische_about_pagina():
    """
    achtergrond informatie staat er over de tools in de About_pagina.html
    :return: als je in de adresbalk /about intypt krijg je de About_pagina.html
    """
    return render_template('About_page.html')

@app.route('/tutorial')
@profile_route
def tutorial_pagina():
    """
    achtergrond informatie staat er over het installeren van de tools in de tutorial_page.html
    :return: als je in de adresbalk /tutorial intypt krijg je de tutorial_page.html
    """
    return render_template('tutorial_page.html')

@app.route('/tool', methods=['GET', 'POST'])
@profile_route
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

        file_path = os.path.join(UPLOAD_FOLDER, f.filename)

        f.save(file_path)
        speed = request.form.get('speed', '')  # Default to an empty string if not set
        model = request.form.get('model', '') 

        fasttree = FastTree(
            file_path, 
            output_file="output.nw", 
            output_image=os.path.join("static", "tree.png")
        )

        fasttree.run_fasttree()
        fasttree.render_tree_image()

        tree_output = url_for('static', filename='tree.png')
        kwargs = {
            'speed': speed,
            'model': model,
        }

        fasttree.run_fasttree(**kwargs)


        return render_template('tool_output.html', tree=tree_output, **kwargs)


@app.route('/contact', methods=['GET', 'POST'])
@profile_route
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
    app.run()