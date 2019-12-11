import sys


temp = dict()

for line in sys.stdin:
    line = line.replace('\n', '')
    key, value = line.split('\t')

    if temp.get(key):
        temp.update({key: (temp.get(key), value)})
    else:
        temp.update({key: value})

for elem in sorted(temp):
    if temp.get(elem) == 'A':
        print(elem)
