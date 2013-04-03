"""
Songs
"""

class Song(object):
    """ define song infor """
    def __init__(self, song_tuple):
        try:
            self.song_name = song_tuple[0][0]
            self.song_artist = song_tuple[0][1]
            self.song_album = song_tuple[0][2]
            self.song_url = song_tuple[1]

        except ValueError:
            pass

    def get_song_name(self):
        return self.get_song_name

    def get_song_album(self):
        return self.get_song_album

    def get_song_artilst(self):
        return self.get_song_artilst

    def get_song_url(self):
        return self.get_song_url

    
