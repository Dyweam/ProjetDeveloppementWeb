from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('pages/index.html')

@app.route('/artists')
def artists():
    return render_template('pages/artists.html')

@app.route('/albums')
def albums():
    return render_template('pages/albums.html')

@app.route('/genre')
def genre():
    return render_template('pages/genre.html')

@app.route('/clients')
def clients():
    return render_template('pages/clients.html')

@app.route('/commands')
def commands():
    return render_template('pages/commands.html')

@app.route('/employees')
def employees():
    return render_template('pages/employees.html')