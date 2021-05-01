import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}

y, m, d = input('년, 월, 일 순으로 입력하세요. ex) 2020 04 18\n').split()
response = requests.get(
    f'https://www.genie.co.kr/chart/top200?ditc=D&rtm=N&ymd={y}{m}{d}',
    headers=headers
)

# html 가공
soup = BeautifulSoup(response.text, 'html.parser')
selector = '#body-content > div.newest-list > div > table > tbody > tr'
selectors = soup.select(selector)
title_selector = 'td.info > a.title.ellipsis'
artist_selector = 'td.info > a.artist.ellipsis'

rank = 0
for select in selectors:
    title = select.select_one(title_selector).text.strip()
    artist = select.select_one(artist_selector).text.strip()
    if title and artist:
        rank = rank + 1
        print(rank, title, artist)