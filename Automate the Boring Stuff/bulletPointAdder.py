#! python3
# bulletPointAdder.py - クリップボードのテキストの各行に点を打って、
# wikipediaの箇条書きにする

import pyperclip
import sys

text = pyperclip.paste()

# 行を分割して、"- " を行頭に追加する
lines = text.split('\n')
# シェル上で指定したbulletpointを用いる。指定がない場合は '- 'を用いる
if len(sys.argv) > 1:
    bulletpoint = sys.argv[1] + ' '
else:
    bulletpoint = '- '

for i in range(len(lines)):
    lines[i] = bulletpoint + lines[i]

# pyperclip.copyは、リストではなく1つの文字列を引数として受取るため、文字列にまとめる
text = '\n'.join(lines)

pyperclip.copy(text)
