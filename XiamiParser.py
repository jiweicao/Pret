#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib2
import urllib
import logging
from bs4 import BeautifulSoup
from itertools import izip


URL = "http://www.xiami.com"
url_pattern = { "song": "http://www.xiami.com/search/song?",
                "album": "http://www.xiami.com/search/album?",
                "artist": "http://www.xiami.com/search/artist?"}

def url_open(category, name):
    opener = urllib2.build_opener()
    opener.addheaders = [('User-agent', 'Mozilla/5.0'),
                         ('Referer', URL)]

    p = {'key':name.encode('utf-8')}
    url = url_pattern[category] + urllib.urlencode(p)
    html = opener.open(url)
    return BeautifulSoup(html)

def find_song_link(soup):
    for link in soup.find_all('td', "song_name"):
        link = link.find('a', target="_blank")
        yield (URL + link.get('href'))

# category = "song_name", "song_artist", "song_album"
def find_song_info(soup, category):
    for link in soup.find_all('td', class_=category):
        yield reduce(lambda x, y: x + y, link.find_all(text=True))

def search_song(name):
    soup = url_open("song", name)
    for title, artist, album, url in izip(find_song_info(soup, "song_name"),
                                         find_song_info(soup, "song_artist"),
                                         find_song_info(soup, "song_album"),
                                         find_song_link(soup)):
        yield {"title": title,
               "artist": artist,
               "album": album,
               "url": url,
               "id": int(url[len(URL+"/song/"):])
               }

def search_album(name):
    soup = url_open("album", name)
    for link in soup.find_all('div', class_='album_item100_block'):
        artist = link.find('p', class_='name').find('a').get('title')
        url = URL + link.find('p', class_='name').find('a').get('href')
        title = link.find('p', class_='name').find('a').get('title')
        yield {"title": title,
               "artist": artist,
               "url": url,
               "id": int(url[len(URL+"/album/"):])
               }

def search_artist(name):
    soup = url_open("artist", name)
    artist_lst = []
    url_lst = []
    for link in soup.find_all('div', class_='artist_item100_block'):
        url_lst.append(URL + link.find('p', class_='buddy').find('a').get('href'))
        artist_lst.append(link.find('p', class_='name').find('span').get_text())
        
    for name, url in izip(artist_lst, url_lst):
        yield{"name":name,
              "url": url,
              "id":int(url[len(URL+"/artist/"):])
              }

def main():
    name = "kelly"
    print name
    for item in search_song(name):
        print item

if __name__ == "__main__":
    main()
