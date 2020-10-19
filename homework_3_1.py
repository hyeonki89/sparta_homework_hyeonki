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

# 랭크 정보를 가져올 수 있었지만, 만약 랭크 정보가 없이 순서대로 있다면 랭크를 리스트에 추가하는 법
my_rank = 0
for tr in trs:
    # 랭크 정보가 있는 경우
    # rank = tr.select_one('#frm > div > table > tbody > tr:nth-child(1) > td:nth-child(2) > div > span.rank')
    title = tr.select_one('td:nth-child(5) > div > div > div.ellipsis.rank01 > span > a').text
    album = tr.select_one('td:nth-child(6) > div > div > div > a').text
    artist = tr.select_one('td:nth-child(5) > div > div > div.ellipsis.rank02 > a').text
    #랭크를 하나씩 추가해주는 방법
    my_rank = my_rank+1

    my_dict = {
        'rank' : my_rank,
        'title' : title,
        'album' : album,
        'artist' : artist
    }

    db.homework_3_1.insert_one(my_dict)

    print(my_rank,title,album,artist)