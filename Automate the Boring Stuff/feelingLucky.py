#! /usr/bin/env python3

import sys
import requests
import webbrowser
import bs4

# 検索ワード
query = ' '.join(sys.argv[1:])
print('Googling "{}"...'.format(query))
query = '+'.join(sys.argv[1:])

# コマンドラインに入力した引数をjoinしてgoogle検索
res = requests.get('https://www.google.com/search?q=' + query)

# urlを正しく読み込めているかチェック
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text, 'html.parser')
link_elems = soup.select('div.r a')

# 各結果をブラウザのタブで開く
num_open = min(5, len(link_elems)) # 開く結果の数を指定。検索結果の数と5の小さい方
for i in range(num_open):
    print('Opening "https://wwww.google.com{}"...'.format(link_elems[i].get('href')))
    webbrowser.open('https://wwww.google.com' + link_elems[i].get('href'))
