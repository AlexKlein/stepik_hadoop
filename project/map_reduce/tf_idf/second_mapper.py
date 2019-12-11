import sys


for line in sys.stdin:
    line = line.replace('\n', '')

    word, doc, tf = line.split('\t')
    print(word, str(doc) + ';' + str(tf) + ';' + '1', sep='\t')
