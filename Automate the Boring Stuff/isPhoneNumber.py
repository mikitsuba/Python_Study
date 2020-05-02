#! python3
# isPhoneNumber.py - クリップボードから電話番号を検索する

import pyperclip, re

# 電話番号の正規表現
PHONE_REGEX = re.compile(r'''(
(\d{1,4}|\(\d{1,4}\))       # 市外局番。()がついていてもいなくても group(1)
(\s|-|\.)?              # 区切り。空白 or - or . group(2)
(\d{1,4})                 # 1~4桁の番号 group(3)
(\s|-|\.)?              # 区切り。空白 or - or . group(4)
(\d{3,4})                 # 3~4桁の番号 group(5)
(\s*(ext|x|ext.)\s*(\d{2,5}))? # 内線番号2〜5桁 group(6, 7, 8)
)''', re.VERBOSE)

# クリップボードから文字列を取得
text = str(pyperclip.paste())

# 取得した文字列を検索
matches = []
for groups in PHONE_REGEX.findall(text):
    phone_num = ''.join([groups[1], groups[3], groups[5]])
    if groups[8]: # 内線番号がある場合
        phone_num += groups[8] + '（内線）'
    if not groups[8] and (len(phone_num) >= 10): # 総桁数が10以上である場合に限定をかけている。内線番号がある場合は、ext/x/ext.と書いてあるから、間違いなく電話番号という判断 
        matches.append(phone_num)

# 見つかった電話番号をクリップボードに貼り付け
if matches:
    pyperclip.copy('\n'.join(matches)) # pyperclip.copy()は、リストのままの貼り付けには対応していないため、文字列にしている
    print('クリップボードに貼り付けました')
    print('\n'.join(matches))
else:
    print('電話番号は見つかりませんでした')
