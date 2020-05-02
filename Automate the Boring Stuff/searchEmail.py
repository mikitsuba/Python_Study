#! python3
# searchEMAIL.py - クリップボードから電話番号を検索する

import pyperclip, re

# EMAILの正規表現
EMAIL_REGEX = re.compile('[0-9a-z_./?-]+@[0-9a-z-]+\.+[0-9a-z-]+')

# クリップボードから文字列を取得
text = str(pyperclip.paste())

# 取得した文字列を検索
matches = []
for email in EMAIL_REGEX.findall(text):
    matches.append(email)

# 見つかったEMAILをクリップボードに貼り付け
if matches:
    pyperclip.copy('\n'.join(matches)) # pyperclip.copy()は、リストのままの貼り付けには対応していないため、文字列にしている
    print('クリップボードに貼り付けました')
    print('\n'.join(matches))
else:
    print('EMAILアドレスは見つかりませんでした')
