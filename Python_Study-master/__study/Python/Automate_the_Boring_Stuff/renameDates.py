#!/usr/bin/env python3
# renameDates.py - 米国式日付MM-DD-YYYYのファイル名を日本式YYYY-MM-DDに書き換える

import shutil
import os
import re

# 米国式のテキストパターンを識別する正規表現を作成する
DATE_REGEX = re.compile(r"""^(.*?) # 日付前のテキスト（非貪欲マッチ） group(1)
                            ([0|1]?\d)- # 月を表す1~2桁の数字。01も1も拾う group(2)
                            ([0-3]?\d)- # 日を表す1~2桁の数字。01も1も拾う group(3)
                            ([19|20]\d{2}) # 年を表す4桁の数字。1900年〜2099年まで group(4)
                            (.*?)$ # 日付後のテキスト（非貪欲マッチ） group(5)
                        """, re.VERBOSE)

# 検索するフォルダのpathを指定
path = "/Users/t-miki/Python/"

# os.listdir()を呼び出し、指定したフォルダの全ファイルを取り出す
# 正規表現を用いて、ファイル名に日付があるか順番に調べる
for filename in os.listdir(path):
    m = DATE_REGEX.search(filename)

    before = m.group(1)
    month = m.group(2)
    date = m.group(3)
    year = m.group(4)
    after = m.group(5)
 
    # 日付があれば、shutil.move()を用いてファイル名を変更する
    if m:
        revised_filename = f'{before}{year}-{month}-{date}{after}'
        print(f'Renaming {filename} to {revised_filename}')
        # shutil.move(filename, revised_filename)
        



