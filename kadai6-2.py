"""

# オープンデータ名と概要:
東京都オープンデータAPI (Tokyo Metropolitan Government Open Data API)  
このAPIは、東京都が提供する公共施設、文化財、スポーツ施設、WiFiアクセスポイントなど、多種多様なデータを利用者に提供する。

# エンドポイントと機能:
API ベースURL: https://api.data.metro.tokyo.lg.jp/v1  
例えば、以下のエンドポイントが利用可能です:
- 公共施設情報: GET /PublicFacility
- 文化財一覧: GET /CulturalProperty
# 使い方:
APIキーは必要ない。必要なエンドポイントを指定してデータをリクエストするだけで、情報を取得可能。
"""

import requests

def get_public_Cultural_data():
    url = "https://api.data.metro.tokyo.lg.jp/v1/CulturalProperty"
    params ={
        "名称.表記": "木造釈迦三尊及び五百羅漢等像"
    }
    response = requests.get(url,params=params)
    data = response.json()
    return data

if __name__ == "__main__":
    Cultural_data = get_public_Cultural_data()
    if Cultural_data:
        print("取得したデータ:")
        print(Cultural_data)
    else:
        print("データの取得に失敗しました。")
