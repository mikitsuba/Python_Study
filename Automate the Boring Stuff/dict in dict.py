all_guests = {'アリス': {'りんご': 5, 'うんこ': 3}, 
'ボブ': {'ハムサンド': 3, 'りんご': 2},
'キャロル': {'コップ': 3, 'アップルパイ': 1}}


def total_brought(guests, item):
    num_brought = 0
    for k, v in guests.items():
        num_brought = num_brought + v.get(item, 0)
    return num_brought

print('持ち物の数:')
print('- りんご' + str(total_brought(all_guests, 'りんご')))
