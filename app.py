from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def home_pagina():
    return render_template('base.html')

@app.route('/about')
def dynamische_about_pagina():
    return render_template('About_page.html')

@app.route('/tutorial')
def tutorial_pagina():
    return render_template('tutorial_page.html')

@app.route('/contact')
def contact_pagina():
    if request.method == 'GET':
        return render_template('contact_page.html')

    elif request.method == 'POST':
      kwargs = {
          'name' : request.form['name'],
          'email' : request.form['email'],
          'message' : request.form['message']
      }
    return render_template('contact_page.html', **kwargs)

if __name__ == '__main__':
    app.run()


if __name__ == '__main__':
    app.run(debug=True)