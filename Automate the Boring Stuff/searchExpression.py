#! /usr/bin/env python3
#! searchExpression.py - フォルダの中のすべてのtxtファイルを開き、指定した正規表現にマッチする行を検索し、結果を画面に表示する

import os, sys, re

# 検索対象のファイル形式
file_type = '.txt'

def search(target_path, regex):
    # フォルダ中の全てのtxtファイルを開く
    for path, _, filenames in os.walk(target_path):
        for filename in filenames:
            file_path = os.path.join(path, filename)
            # target_pathにおいて、file_typeのファイルを検索する
            if filename.endswith(file_type):
                with open(file_path) as f:
                    for row in f.readlines():
                        if re.findall(regex, row):
                            print(f'{filename} というファイルに {row.rstrip()} という行がある')

if __name__ == '__main__':
    target_path = './'
    m = re.compile(sys.argv[1])
    
    search(target_path, m)
    
