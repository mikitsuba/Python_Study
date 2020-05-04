import webbrowser
import sys
import pyperclip
import re

if len(sys.argv) > 1:
    address = ' '.join(sys.argv[1:])
else:
    address = pyperclip.paste()

try:
    print(f'住所は： {address}')
    m = re.compile(r'[a-zA-Z0-9\s,-]+$')
    if not m.match(address):
        raise Exception('半角英数字以外が含まれています')
    webbrowser.open('https://www.google.com/maps/place/' + address)
except Exception as err:
    print(err)
    