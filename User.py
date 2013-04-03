"""
User
"""
import Admin
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
    Admin.delete_user_byname("adam")
    Admin.delete_all_byid(13)

if __name__ == "__main__":
    main()
