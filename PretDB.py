import os

PATH = '/Users/jiweicao/Dropbox/waker/redis-2.6.9/src/'
class PretDB(object):
    @staticmethod
    def start_db():
        os.system(PATH + 'redis-server')
    
    @staticmethod
    def close_db():
        os.system(PATH + 'redis-cli shutdown')

if __name__ == "__main__":
    PretDB.start_db()
