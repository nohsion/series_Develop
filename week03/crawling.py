import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}

response = requests.get(
    'https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=pnt&date=20200716',
    headers=headers
)
# print(response.text)

# html 가공
soup = BeautifulSoup(response.text, 'html.parser')
selector = '#old_content > table > tbody > tr'
title_selector = 'td.title > div > a'
titles = soup.select(selector)

point_selector = 'td.point'
points = soup.select(selector)

rank = 0
for title in titles:
    title_tag = title.select_one(title_selector)
    point_tag = title.select_one(point_selector)

    if title_tag and point_tag:
        rank = rank + 1
        print(format(rank, '02d'), title_tag.text, point_tag.text)


