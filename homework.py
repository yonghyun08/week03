import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient

client = MongoClient('localhost',27017)
db = client.dbsparta

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.genie.co.kr/chart/top200?ditc=D&rtm=N&ymd=20200713',headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

musicList = soup.select('#body-content > div.newest-list > div > table > tbody > tr')
for list in musicList:
    rank = list.select_one('tr> td.number').text[:3].strip()
    title = list.select_one('tr > td.info > a.title.ellipsis').text.strip()
    artist = list.select_one('tr > td.info > a.artist.ellipsis').text
    db.musicList.insert_one({'rank':rank,'title':title,'artist':artist})


