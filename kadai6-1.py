
import requests

APP_ID = "29b953c23d86a2bae71750a52a2d37cd8f565c9b"
API_URL = "http://api.e-stat.go.jp/rest/3.0/app/json/getStatsData"#エンドポイント

params = {
    "appId": APP_ID,
    "statsDataId": "0003109558",#簡易生命表を指定
    "cdArea": "2023000000",#時間軸（年次）の2023年を指定
    "cdCat01": "410500",#年齢区分を105～年に指定
    "lang": "J"  # 日本語を指定
}

#response = requests.get(API_URL, params=params)
response = requests.get(API_URL, params=params)
# Process the response
data = response.json()
print(data)

"""
取得したデータの種類：簡易生命表
エンドポイント：エンドポイントはhttp://api.e-stat.go.jp/rest/3.0/app/json/getStatsData
機能：簡易生命表の中から時間軸が2023年で指定され、年齢区分が105～年であるものをapiを利用して表示する
使い方：python3 kadai6-1.pyとターミナルで入力する
"""
