"""
Admin 
"""
import redis
from hashlib import md5
from User import User
from Song import Song

r = redis.Redis("localhost")

def get_next_id():
    id = r.lpop("emptyID")
    if id:
        return int(id)
    return r.incr("nextUserId")

def add_user(user):
    if isinstance(user, User):
        id = get_next_id()
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
        id = song.url - "http://www.xiami.com/song/"
        if int(id):
            id = int(id)
            r.set("songid:%d:name" % id, song.song_name)
            r.set("songid:%d:album" % id, song.song_album)
            r.set("songid:%d:url" % id, song.song_url)
            r.set("songid:%d:artist" % id, song.song_artist)
            r.set("songname:%s:songid" %song.song_name, id)
        else:
            return False

#delete song from redis
def delete_song_id(id):
    # wheter the song is in redis or not
    #if 
    

    
if __name__ == "__main__":
    adam = User("adam", "Adam Smith", "wealthofnations")
    add_user(adam)
    #admin.delete_user_username("adam")
    #print admin.r.lpop("emptyID")


            
            
