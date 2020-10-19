from pymongo import MongoClient
import requests
from bs4 import BeautifulSoup


client = MongoClient('localhost', 27017)
db = client.dbsparta



headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}

data = requests.get('https://www.melon.com/new/index.htm', headers=headers)
soup = BeautifulSoup(data.text, 'html.parser')
trs = soup.select('#frm > div > table > tbody > tr')

my_data = []

my_rank = 0
for tr in trs:
    # rank = tr.select_one('#frm > div > table > tbody > tr:nth-child(1) > td:nth-child(2) > div > span.rank')
    title = tr.select_one('td:nth-child(5) > div > div > div.ellipsis.rank01 > span > a').text
    album = tr.select_one('td:nth-child(6) > div > div > div > a').text
    artist = tr.select_one('td:nth-child(5) > div > div > div.ellipsis.rank02 > a').text
    my_rank = my_rank+1
    my_dict = {
        'rank' : my_rank,
        'title' : title,
        'album' : album,
        'artist' : artist
    }

    print(my_rank,title,album,artist)