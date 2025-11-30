import json

filename = 'numbers.json'

try:
    with open(filename) as f:
        print(json.load(f))

except FileNotFoundError:
    print('File not found!')