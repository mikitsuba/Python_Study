#! /usr/bin/env python3
# backpToZip.py - フォルダ全体を連番付きZIPファイルにコピーする

import zipfile
import os
import shutil
import datetime

# バックアップ対象のフォルダ
folder = '/Users/mikitsuba/Programming/__study/' 

# バックアップ後のファイルの名称
folder = os.path.abspath(folder) # folderを絶対パスにする
now = datetime.datetime.now()
now = now.strftime('%Y%m%d_%H%M%S')
zip_filename = f'{os.path.basename(folder)}_{now}.zip'

def backup_to_zip():
    # フォルダ全体をZIPファイルにバックアップする

    # ZIPファイルを作成する
    print(f'Creating {zip_filename}')
    backup_zip = zipfile.ZipFile(zip_filename, 'w')

    # フォルダのツリーを渡り歩いて、その中のファイルを圧縮する
    for root, _, files in os.walk(folder):
        print(f'Adding files in {root}')

        backup_zip.write(root)
        for file in files:
            new_base = os.path.basename(folder) + ''
            if file.startswith(new_base) and file.endswith('.zip'):
                 continue
            backup_zip.write(os.path.join(root, file))
    backup_zip.close()

    print('Done.')

backup_to_zip()

# バックアップファイルの保存先
storage = '/Users/mikitsuba/Programming/__study/Python/Automate_the_Boring_Stuff/back_up'

# バックアップファイルをバックアップフォルダに移動
shutil.move(zip_filename, storage)



