import os
import requests
import bs4

start_url = 'https://xkcd.com/'

os.makedirs('xkcd', exist_ok=True)

while not start_url.endswith('#'):
    # ページをダウンロードする
    res = requests.get('')

    # コミック画像のURLを見つける
    # 画像をダウンロードする
    # 画像をフォルダに保存する
    # prevボタンのURLを取得する