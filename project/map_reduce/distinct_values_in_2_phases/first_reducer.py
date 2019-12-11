import sys


last_key, count = None, 0
key_set = set()

for line in sys.stdin:
    line = line.replace('\n', '')
    key_pair, value = line.split('\t')
    key_index, key = key_pair.split(',')
    key_set.add((key_index, key))

for elem in sorted(key_set):
    print(elem[0], elem[1], sep=',')
