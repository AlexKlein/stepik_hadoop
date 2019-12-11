import sys


for line in sys.stdin:
    line = line.replace('\n', '')
    key, user, site = line.split('\t')

    print(site.strip())
