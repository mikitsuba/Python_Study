def is_phone_number(text):
    if len(text) != 12:
        return False
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False
        if text[3] != '-':
            return False
    for i in range(4, 7):
        if not text[i].isdecimal():
            return False
        if text[7] != '-':
            return False
    for i in range(8, 12):
        if not text[i].isdecimal():
            return False
    return True
        
print('番号を入力してください')
digits = input()

if is_phone_number(digits):
    print(f'{digits}は電話番号です')
else:
    print('出直せクソが')