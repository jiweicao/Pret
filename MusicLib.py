"""
Songs
"""
class Song(object):
    """ define song info """
    def __init__(self, song_dict):
        try:
            self.song_title = song_dict["title"]
            self.song_artist = song_dict["artist"]
            self.song_album = song_dict["album"]
            self.song_url = song_dict["url"]

        except ValueError:
            return False 

    def get_song_title(self):
        return self.song_title

    def get_song_album(self):
        return self.song_album

    def get_song_artilst(self):
        return self.song_artist

    def get_song_url(self):
        return self.song_url

class Album(object):
    """ define Album info"""
    def __init__(self, album_dict):
        try:
            self.album_title = album_dict["title"]
            self.album_artist = album_dict["artist"]
            self.album_url = album_dict["url"]
        except ValueError:
            return False

class Artist(object):
    """define Artist info"""
    def __init__(self, artist_dict):
        try:
            self.artist_name = artist_dict["name"]
            self.artist_url = artist_dict["url"]
        except ValueError:
            return False

