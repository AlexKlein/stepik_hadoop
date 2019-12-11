import re
import sys


for line in sys.stdin:
    line = line.replace('\n', '')
    doc = line[:line.find(':')]
    line = re.sub(r'^[\d*:]*', '', line)

    for token in re.split(r'[- :.,!?\t]', line):
        if token:
            print(token + '#' + doc, 1, sep='\t')
