""""
# オープンデータ名と概要:
漁業センサス
このAPIは、流通加工業における魚市場の数について提供している
# エンドポイント
API ベースURL:http://api.e-stat.go.jp/rest/3.0/app/json
例えば以下のようなエンドポイントを使用可能である
メタ情報: /getMetaInfo
統計データ: /getStatsData
#使い方
APP_IDを合わせて必要なエンドポイントを指定してデータをリクエストすることで、情報を取得可能
"""
import requests

APP_ID = "e740eb2247dff5f8c0b8c0dcad40b41c669abfc1"
API_URL = "http://api.e-stat.go.jp/rest/3.0/app/json/getStatsData"

params ={
    "appId": APP_ID,
    "statsDataId": "0001822415",#2018年漁業センサス/流通加工業/魚市場数
    "statsCode": "00500210",
    "searchWord": "累計",
    "openYeaars": 20210322,
    "limit": 2,
    "lang": "J"
}

#エンドポイント
response = requests.get(API_URL,params=params)

data = response.json()
print(data)
