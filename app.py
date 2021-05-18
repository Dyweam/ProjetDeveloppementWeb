from flask import Flask, render_template
app = Flask(__name__)

from peewee import *
# SQLite database using WAL journal mode and 64MB cache.
sqlite_db = SqliteDatabase('chinook.db', pragmas={'journal_mode': 'wal','cache_size': -1024 * 64})

class BaseModel(Model):
    class Meta:
        database = sqlite_db

class Genres(BaseModel):
    Genreid = AutoField()
    Name = CharField()
    class Meta:
        table_name = 'genres'

query = Genres.select(Genres.Genreid, Genres.Name)
for genre in query:
    print(genre.Name)

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