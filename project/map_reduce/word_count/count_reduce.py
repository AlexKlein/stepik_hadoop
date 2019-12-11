import sys


(last_key, running_sum) = (None, 0)

for line in sys.stdin:
    (key, value) = line.split('\t')

    if last_key and last_key != key:
        print(last_key, str(running_sum), sep='\t')
        (last_key, running_sum) = (key, int(value))
    else:
        (last_key, running_sum) = (key, running_sum + int(value))

if last_key:
    print(last_key, str(running_sum), sep='\t')
