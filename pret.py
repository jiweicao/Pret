"""
Admin 
"""
from PretDB import PretDB
import XiamiParser

class Pret(object):
    def __init__(self):
        pass
    def start(self):
        PretDB.start_db()
    def close(self):
        PretDB.close_db()

    def search(self, query):
        ret = {}
        ret["songs"] = list(XiamiParser.search_song(query))
        ret["albums"] = list(XiamiParser.search_album(query))

if __name__ == "__main__":
    machine = Pret()
    a = machine.search("kelly")
    print a


            
            
