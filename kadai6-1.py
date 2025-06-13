import requests

APP_ID = "e740eb2247dff5f8c0b8c0dcad40b41c669abfc1"
API_URL = "http://api.e-stat.go.jp/rest/3.0/app/json/getStatsData"

params ={
    "appId": APP_ID,
    "statsDataId": "0001822415",#2018年漁業センサス/流通加工業/魚市場数
    "cdArea": "1988000000",
    "lang": "J"
}

#エンドポイント
response = requests.get(API_URL,params=params)

data = response.json()
print(data)
