from lib.album_repo import AlbumRepo
from lib.album import Album

"""
When we call AlbumRepository#all
We get a list of Album objects reflecting the seed data.
"""
def test_get_all_records(db_connection):
	db_connection.seed("seeds/music_library.sql")
	repo = AlbumRepo(db_connection)

	albums = repo.all()

	assert albums == [
		Album(1, 'Doolittle', 1989, 1),
		Album(2, 'Surfer Rosa', 1988, 1),
		Album(3, 'Waterloo', 1974, 2),
		Album(4, 'Super Trouper', 1980, 2),
		Album(5, 'Bossanova', 1990, 1),
		Album(6, 'Lover', 2019, 3),
		Album(7, 'Folklore', 2020, 3),
		Album(8, 'I Put a Spell on You', 1965, 4),
		Album(9, 'Baltimore', 1978, 4),
		Album(10, 'Here Comes the Sun', 1971, 4),
		Album(11, 'Fodder on My Wings', 1982, 4),
		Album(12, 'Ring Ring', 1973, 2),
	]

def test_find_record_by_id(db_connection):
	db_connection.seed("seeds/music_library.sql")
	repo = AlbumRepo(db_connection)

	result = repo.find(id=3)

	assert result == Album(3, 'Waterloo', 1974, 2)

def test_create_record(db_connection):
	db_connection.seed("seeds/music_library.sql")
	repo = AlbumRepo(db_connection)

	repo.create(Album(None, "Voulez-Vous", 1979, 2))

	result = repo.all()

	assert result == [
		Album(1, 'Doolittle', 1989, 1),
		Album(2, 'Surfer Rosa', 1988, 1),
		Album(3, 'Waterloo', 1974, 2),
		Album(4, 'Super Trouper', 1980, 2),
		Album(5, 'Bossanova', 1990, 1),
		Album(6, 'Lover', 2019, 3),
		Album(7, 'Folklore', 2020, 3),
		Album(8, 'I Put a Spell on You', 1965, 4),
		Album(9, 'Baltimore', 1978, 4),
		Album(10, 'Here Comes the Sun', 1971, 4),
		Album(11, 'Fodder on My Wings', 1982, 4),
		Album(12, 'Ring Ring', 1973, 2),
		Album(13, "Voulez-Vous", 1979, 2)
	]

def test_delete_record(db_connection):
	db_connection.seed("seeds/music_library.sql")
	repo = AlbumRepo(db_connection)

	repo.delete(album_id=6) # No apologies to Taylor Swift fans

	result = repo.all()

	assert result == [
		Album(1, 'Doolittle', 1989, 1),
		Album(2, 'Surfer Rosa', 1988, 1),
		Album(3, 'Waterloo', 1974, 2),
		Album(4, 'Super Trouper', 1980, 2),
		Album(5, 'Bossanova', 1990, 1),
		Album(7, 'Folklore', 2020, 3),
		Album(8, 'I Put a Spell on You', 1965, 4),
		Album(9, 'Baltimore', 1978, 4),
		Album(10, 'Here Comes the Sun', 1971, 4),
		Album(11, 'Fodder on My Wings', 1982, 4),
		Album(12, 'Ring Ring', 1973, 2),
	]