import urllib.robotparser

import requests
import pprint
import secret

# HTTP GET request
# response = requests.get(
#     'http://openapi.seoul.go.kr:8088/6d4d776b466c656533356a4b4b5872/json/RealtimeCityAir/1/99'
# )

# result = response.json()
# # print(result)
# data = result['RealtimeCityAir']['row']
#
# for datum in data:
#     state = datum['MSRSTE_NM']
#     pm10 = datum['PM10']
#     if pm10 > 25:
#         # f-string
#         print(f'{state} - {pm10}')

# 책정보 naver api
book_name = '프리워커스'
naver_url = f'https://openapi.naver.com/v1/search/book.json?query={book_name}'
headers = {
    'X-Naver-Client-Id': secret.client_id,
    'X-Naver-Client-Secret': secret.client_secret,
}
res = requests.get(
    naver_url,
    headers=headers,
)

# 파파고 정보 naver api
papago_url = 'https://openapi.naver.com/v1/papago/n2mt'
papago_text = '난 정말 네가 좋아, 꼬마개구리'
data = {
    'source': 'ko',
    'target': 'en',
    'text': papago_text,
}
response = requests.post(
    papago_url,
    headers=headers,
    data=data
)

result = response.json()
print(result['message']['result']['translatedText'])
