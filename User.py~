# redis
# http://degizmo.com/2010/03/23/redis-relations-in-a-nosql-world/
import redis
from hashlib import md5
from sets import *

class User(object):
    """define users info"""
    def __init__(self, username, fullname, password, followers=Set([]), following=Set([])):
        self.userid = -1
        self.username = username
        self.fullname = fullname
        self.password = password
        self.followers = followers
        self.following = following
    
    def get_followers(self):
        return self.followers

    def get_following(self):
        return self.following

    def get_userid(self):
        return self.userid

def main():
    admin = Admin("jiwei")
    admin.delete_user("adam")
    admin.delete_all_users()
    print admin.get_next_id()
    '''
    adam = User("adam", "Adam Smith", "wealthofnations")
    admin.add_user(adam)
    carol = User("carol", "Carol Burnett", "eartug")
    admin.add_user(carol)
    '''

if __name__ == "__main__":
    main()
