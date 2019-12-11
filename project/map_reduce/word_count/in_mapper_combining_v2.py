import sys


temp = dict()

for line in sys.stdin:
    line = line.replace('\n', '')

    for token in line.split(' '):
        if token:
            if temp.get(token):
                temp.update({token: temp.get(token) + 1})
            else:
                temp.update({token: 1})

for key in temp:
    print(key, temp[key], sep='\t')
