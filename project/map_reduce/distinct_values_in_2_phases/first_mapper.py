import sys


for line in sys.stdin:
    line = line.replace('\n', '')
    key, value_list = line.split('\t')
    for value in str(value_list).split(','):
        print(key + ',' + value, 1, sep='\t')
