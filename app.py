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
    UnitPrice = DecimalField()
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
    BillingState = CharField()
    BillingCountry = CharField()
    BillingPostalCode = CharField()
    Total = DecimalField()
    class Meta:
        table_name = 'invoices'

class InvoicesItems(BaseModel):
    InvoiceItemId = AutoField()
    InvoiceId = IntegerField()
    TrackId = IntegerField()
    UnitPrice = DecimalField()
    Quantity = IntegerField()
    class Meta:
        table_name = 'invoice_items'

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
    City = CharField()
    State = CharField()
    Country = CharField()
    PostalCode = CharField()
    Phone = CharField()
    Fax = CharField()
    Email = CharField()
    class Meta:
        table_name = 'invoices'

# query = Genres.select(Genres.GenreId, Genres.Name)
# for genre in query:
#     print(genre.Name)

@app.route('/')
def index():
    artistsQuery = Artists.select(Artists.ArtistId, Artists.Name).limit(5)
    albumsQuery = Albums.select(Albums.AlbumId, Albums.Title).limit(5)
    genresQuery = Genres.select(Genres.GenreId, Genres.Name).limit(5)

    artists = []
    for artist in artistsQuery:
        artists.append([artist, artist.Name])

    albums = []
    for album in albumsQuery:
        albums.append([album, album.Title])

    genres = []
    for genre in genresQuery:
        genres.append([genre, genre.Name])

    return render_template('pages/index.html', artists = artists, albums = albums, genres = genres)

#####

@app.route('/artists')
def artists():
    artistsQuery = Artists.select(Artists.ArtistId, Artists.Name)
    artists = []
    for artist in artistsQuery:
        artists.append([artist, artist.Name])
    return render_template('pages/artists.html', artists = artists)

@app.route('/artist/<id>', methods=['GET'])
def artist(id):
    artistsQuery = Artists.select(Artists.ArtistId, Artists.Name).where(Artists.ArtistId == id)
    artists = []
    for artist in artistsQuery:
        artists.append([artist, artist.Name])

    albumsQuery = Albums.select(Albums.AlbumId, Albums.Title).where(Albums.ArtistId == id)
    albums = []
    for album in albumsQuery:
        albums.append([album, album.Title])

    return render_template('pages/artist.html', artist = artists[0], albums = albums)

#####

@app.route('/albums')
def albums():
    albumsQuery = Albums.select(Albums.AlbumId, Albums.Title)
    albums = []
    for album in albumsQuery:
        albums.append([album, album.Title])
    return render_template('pages/albums.html', albums = albums)

@app.route('/album/<id>', methods=['GET'])
def album(id):
    albumsQuery = Albums.select(Albums.AlbumId, Albums.Title).where(Albums.AlbumId == id)
    albums = []
    for album in albumsQuery:
        albums.append([album, album.Title])

    tracksQuery = Tracks.select(Tracks.TrackId, Tracks.Name).where(Tracks.AlbumId == id)
    tracks = []
    for track in tracksQuery:
        tracks.append([track, track.Name])

    return render_template('pages/album.html', album = albums[0], tracks = tracks)

#####

@app.route('/genres')
def genres():
    genresQuery = Genres.select(Genres.GenreId, Genres.Name).limit(5)
    genres = []
    for genre in genresQuery:
        genres.append([genre, genre.Name])
    return render_template('pages/genres.html', genres = genres)

@app.route('/genre/<id>', methods=['GET'])
def genre(id):
    genresQuery = Genres.select(Genres.GenreId, Genres.Name).where(Genres.GenreId == id)
    genres = []
    for genre in genresQuery:
        genres.append([genre, genre.Name])

    tracksQuery = Tracks.select(Tracks.TrackId, Tracks.Name).where(Tracks.GenreId == id)
    tracks = []
    for track in tracksQuery:
        tracks.append([track, track.Name])
    return render_template('pages/genre.html', genre = genres[0], tracks = tracks)

#####

@app.route('/clients')
def clients():
    clientsQuery = Customers.select(Customers.CustomerId, Customers.FirstName, Customers.LastName)
    clients = []
    for client in clientsQuery:
        clients.append([client, client.FirstName, client.LastName])
    return render_template('pages/clients.html', clients = clients)

@app.route('/client/<id>', methods=['GET'])
def client(id):
    clientsQuery = Customers.select(Customers.CustomerId, Customers.FirstName, Customers.LastName).where(Customers.CustomerId == id)
    clients = []
    for client in clientsQuery:
        clients.append([client, client.FirstName, client.LastName])

    invoicesQuery = Invoices.select(Invoices.InvoiceId, Invoices.Total).where(Invoices.CustomerId == id)
    invoices = []
    for invoice in invoicesQuery:
        invoices.append([invoice, invoice.Total])
    return render_template('pages/client.html', client = clients[0], invoices = invoices)

#####

@app.route('/invoices')
def invoices():
    invoicesQuery = Invoices.select(Invoices.InvoiceId, Invoices.Total, Invoices.InvoiceDate)
    invoices = []
    for invoice in invoicesQuery:
        invoices.append([invoice, invoice.Total, invoice.InvoiceDate])
    return render_template('pages/invoices.html', invoices = invoices)

@app.route('/invoice/<id>', methods=['GET'])
def invoice(id):
    invoicesQuery = Invoices.select(Invoices.InvoiceId, Invoices.Total, Invoices.InvoiceDate).where(Invoices.InvoiceId == id)
    invoices = []
    for invoice in invoicesQuery:
        invoices.append([invoice, invoice.Total, invoice.InvoiceDate])

    invoiceItemsQuery = InvoicesItems.select(InvoicesItems.InvoiceItemId, InvoicesItems.TrackId, InvoicesItems.UnitPrice, InvoicesItems.Quantity).where(InvoicesItems.InvoiceItemId == id)
    invoiceItems = []
    for invoiceItem in invoiceItemsQuery:
        invoiceItems.append([invoiceItem, invoiceItem.TrackId, invoiceItem.UnitPrice, invoiceItem.Quantity])
    return render_template('pages/invoice.html', invoice = invoices[0], invoiceItems = invoiceItems)

#####

@app.route('/employees')
def employees():
    return render_template('pages/employees.html')