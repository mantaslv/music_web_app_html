import os
from flask import Flask, render_template
from lib.album_repo import AlbumRepo
from lib.database_connection import get_flask_database_connection
from lib.artist_repo import ArtistRepo

app = Flask(__name__)

@app.route('/albums', methods=['GET'])
def get_albums():
    conn = get_flask_database_connection(app)
    album_repo = AlbumRepo(conn)
    rows = album_repo.all()

    return render_template('albums.html', albums=rows)


@app.route('/albums/<id>', methods=['GET'])
def get_album_by_id(id):
    conn = get_flask_database_connection(app)
    album_repo = AlbumRepo(conn)
    album = album_repo.find(id)
    artist_repo = ArtistRepo(conn)
    artist_name = artist_repo.find(album.artist_id).name

    return render_template('album_by_id.html', album=album, artist_name=artist_name)


if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))