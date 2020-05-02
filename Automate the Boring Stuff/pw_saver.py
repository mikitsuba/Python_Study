#! python3
# pw_saver.py - パスワード管理プログラム（脆弱性あり）

import sys, pyperclip

PASSWORDS = {'default': 'tsubasa4997',
'bank': '1059'}

if len(sys.argv) < 2:
    print('使い方：python pw_saver.py [アカウント名]')
    print('パスワードをクリップボードにコピーします')
    sys.exit()

account = sys.argv[1] # 最初のコマンドライン引数がアカウント名

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print(f'{account}のパスワードをクリップボードにコピーしました')
else:
    print('{}というアカウント名はありません'.format(account))
