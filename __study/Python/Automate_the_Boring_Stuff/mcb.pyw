#! /usr/bin/env python3
# mcb.pyw - クリップボードのテキストを保存・復元

import shelve, pyperclip, sys

mcb_shelf = shelve.open('mcb')

# クリップボードの内容を保存
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcb_shelf[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 2:
    # キーワード一覧
    if sys.argv[1].lower() == 'list':
        print(*(key for key in mcb_shelf.keys()))
    # キーワード内容の読み込み
    elif sys.argv[1] in mcb_shelf:
        pyperclip.copy(mcb_shelf[sys.argv[1]])

mcb_shelf.close()