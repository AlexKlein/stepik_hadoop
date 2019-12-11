import sys


for line in sys.stdin:
    line = line.replace('\n', '')
    key, user, site = line.split('\t')

    if user.strip() == 'user10':
        print(key.strip(), user.strip(), site.strip(), sep='\t')
