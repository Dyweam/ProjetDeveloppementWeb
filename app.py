from flask import Flask, render_template
app = Flask(__name__)

from peewee import *
# SQLite database using WAL journal mode and 64MB cache.
sqlite_db = SqliteDatabase('chinook.db', pragmas={'journal_mode': 'wal','cache_size': -1024 * 64})

class BaseModel(Model):
    class Meta:
        database = sqlite_db

class Genres(BaseModel):
    GenreId = AutoField()
    Name = CharField()
    class Meta:
        table_name = 'genres'

class MediaTypes(BaseModel):
    MediaTypesId = AutoField()
    Name = CharField()
    class Meta:
        table_name = 'media_types'

class Playlists(BaseModel):
    PlaylistId = AutoField()
    Name = CharField()
    class Meta:
        table_name = 'playlists'

class PlaylistTrack(BaseModel):
    PlaylistId = IntegerField()
    TrackId = IntegerField()
    class Meta:
        table_name = 'playlist_track'

class Tracks(BaseModel):
    TrackId = AutoField()
    Name = CharField()
    AlbumId = IntegerField()
    MediaTypeId = IntegerField()
    GenreId = IntegerField()
    Composer = CharField()
    Milliseconds = IntegerField()
    Bytes = IntegerField()
    UnitPrice = MoneyField()
        class Meta:
        table_name = 'tracks'

class Artists(BaseModel):
    ArtistId = AutoField()
    Name = CharField()
    class Meta:
        table_name = 'artists'

class Invoices(BaseModel):
    InvoiceId = AutoField()
    CustomerId = IntegerField()
    InvoiceDate = DateTimeField()
    BillingAddress = CharField()
    BillingCity = CharField()
    # 4 Classes Supplémentaires
    class Meta:
        table_name = 'invoices'

class InvoicesItems(BaseModel):
    InvoiceItemId = AutoField()
    InvoiceId = IntegerField()
    TrackId = IntegerField()
    UnitPrice = MoneyField()
    Quantity = IntegerField()
    class Meta:
        table_name = 'invoices_items'

class Albums(BaseModel):
    AlbumId = AutoField()
    Title = CharField()
    ArtistId = IntegerField()
    class Meta:
        table_name = 'albums'

class Customers(BaseModel):
    CustomerId = AutoField()
    FirstName = CharField()
    LastName = CharField()
    Company = CharField()
    Address = CharField()
    City = CharField()
    State = CharField()
    Country = CharField()
    PostalCode = CharField()
    Phone = CharField()
    Fax = CharField()
    Email = CharField()
    SupportRepId = IntegerField()
    class Meta:
        table_name = 'customers'

class Employees(BaseModel):
    EmployeesId = AutoField()
    LastName = CharField()
    FirstName = CharField()
    Title = CharField()
    ReportsTo = IntegerField()
    BirthDate = DateTimeField()
    HireDate = DateTimeField()
    Address = CharField()
    # 7 Classes Supplémentaires
    class Meta:
        table_name = 'invoices'

query = Genres.select(Genres.GenreId, Genres.Name)
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