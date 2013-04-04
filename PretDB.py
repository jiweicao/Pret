import redis
import os
from hashlib import md5
from User import User
from MusicLib import Song, Album, Artist

r = redis.Redis("localhost")

SERVER_PATH = '/Users/jiweicao/Dropbox/waker/redis-2.6.9/src/redis-server'
CLIENT_PATH = '/Users/jiweicao/Dropbox/waker/redis-2.6.9/src/redis-cli shutdown'

def get_next_userid():
    id = r.lpop("emptyID")
    if id:
        return int(id)
    return r.incr("nextUserId")

def add_user(user):
    if isinstance(user, User):
        id = get_next_userid()
        r.set("uid:%d:username" % id, user.username)
        r.set("uid:%d:fullname" % id, user.fullname)
        r.set("uid:%d:password" % id, user.password)
        r.set("uid:%d:followers" % id, user.followers)
        r.set("uid:%d:following" % id, user.following)
        r.set("username:%s:uid" %user.username, id) 
    else:
        return False

#delte user by id
def delete_user_byid(id):
    # whether the id is in the redis or not
    r.rpush("emptyID", id)
    username = r.get("uid:%d:username" % id)
    r.delete("uid:%d:username" % id)
    r.delete("uid:%d:password" % id)
    r.delete("uid:%d:followers" % id)
    r.delete("uid:%d:following" % id)
    r.delete("username:%s:uid" % username)

# delete user by username
def delete_user_byname(username):
    id = r.get("username:%s:uid" %username)
    delete_user_id(int(id))

# add song into redis
def add_song(song):
    if isinstance(song, Song):
        r.set("songid:%d:title" % id, song.song_title)
        r.set("songid:%d:album" % id, song.song_album)
        r.set("songid:%d:url" % id, song.song_url)
        r.set("songid:%d:artist" % id, song.song_artist)
        r.set("songname:%s:songid" %song.song_name, id)
    else:
        return False

# add album into redis
def add_album(album):
    if isinstance(album, Album)
def add_songs(songs_list):
    for song in song_list:
        add_song(song)

def add_
class PretDB(object):
    @staticmethod
    def start_db():
        os.system(SERVER_PATH)
    
    @staticmethod
    def close_db():
        os.system(CLIENT_PATH)
        
if __name__ == "__main__":
    adam = User("adam", "Adam Smith", "wealthofnations")
    add_user(adam)
