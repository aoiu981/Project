import requests
from bs4 import BeautifulSoup as bs

URL = 'https://www.melon.com/genre/song_list.htm?gnrCode=GN0100'

header = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36"}
request = requests.get(URL, headers=header)

html = request.text

soup = bs(html, 'html.parser')

song_bs = soup.select('.ellipsis.rank01 > span > a')
songs = []
for song in song_bs:
    songs.append(song.text)


print(songs)