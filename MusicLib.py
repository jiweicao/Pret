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
            self.song_id = song_id["id"]

        except ValueError:
            return False 

class Album(object):
    """ define Album info"""
    def __init__(self, album_dict):
        try:
            self.album_title = album_dict["title"]
            self.album_artist = album_dict["artist"]
            self.album_url = album_dict["url"]
            self.album_id = album_dict["id"]
        except ValueError:
            return False

class Artist(object):
    """define Artist info"""
    def __init__(self, artist_dict):
        try:
            self.artist_name = artist_dict["name"]
            self.artist_url = artist_dict["url"]
            self.artist_id = artist_dict["id"]
        except ValueError:
            return False
