import sys


key_list = list()

for line in sys.stdin:
    line = line.replace('\n', '')
    value, key = line.split(',')
    key_list.append(key)

for elem in sorted(key_list):
    print(elem, 1, sep='\t')
