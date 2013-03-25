"""
Admin 
"""
import redis
from hashlib import md5
from User import User

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
def delete_user_id(self, id):
    r.rpush("emptyID", id)
    username = r.get("uid:%d:username" % id)
    r.delete("uid:%d:username" % id)
    r.delete("uid:%d:password" % id)
    r.delete("uid:%d:followers" % id)
    r.delete("uid:%d:following" % id)
    r.delete("username:%s:uid" % username)

# delete user by username
def delete_user_username(username):
    id = r.get("username:%s:uid" %username)
    delete_user_id(int(id))
    
if __name__ == "__main__":
    adam = User("adam", "Adam Smith", "wealthofnations")
    add_user(adam)
    #admin.delete_user_username("adam")
    #print admin.r.lpop("emptyID")
