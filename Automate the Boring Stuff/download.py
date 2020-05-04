import os
import requests
import bs4
import logging

logging.basicConfig(level=logging.DEBUG, format='%(levelname)s : %(asctime)s : %(message)s')

logging.disable(logging.CRITICAL)

start_url = 'https://xkcd.com/'

os.makedirs('xkcd', exist_ok=True)

while not start_url.endswith('#'):
    # ページをダウンロードする
    res = requests.get(start_url)
    res.raise_for_status()

    # コミック画像のURLを見つける
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    elems = soup.select('#comic img')
    logging.info('{} items found'.format(len(elems)))

    # 画像をダウンロードする
    
    if elems == []:
        print('NO image file was found on {}.'.format(start_url))
    else:
        for elem in elems:
            try:
                comic_url = 'http:' + elem.get('src')
                res = requests.get(comic_url)
                res.raise_for_status()
                logging.info('comic_url: {}'.format(comic_url))

                # 画像をフォルダに保存する
                logging.info('Starting to store the image file.')
                image_file = open(os.path.join('xkcd', os.path.basename(comic_url)), 'wb')
                for chunk in res.iter_content(100000):
                    image_file.write(chunk)
                image_file.close()
            except Exception as err:
                print('{0}   {1}'.format(err, start_url))

    # prevボタンのURLを取得する
    logging.info('Getting the url link for the previous button')
    prev_link = soup.select('a[rel="prev"]')[0]
    prev_url = 'https://xkcd.com/' + prev_link.get('href')
    start_url = prev_url

print('Done.')

