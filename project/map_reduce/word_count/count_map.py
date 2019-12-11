import sys


for line in sys.stdin:
    line = line.replace('\n', '')
    for token in line.split(' '):
        if token:
            print(token, 1, sep='\t')
