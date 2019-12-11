import sys


union_set = set()

for line in sys.stdin:
    line = line.replace('\n', '')
    key, value = line.split('\t')

    union_set.add(key)

for elem in sorted(union_set):
    print(elem)
