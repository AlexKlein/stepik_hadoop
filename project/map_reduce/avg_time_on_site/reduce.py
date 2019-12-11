import sys


last_key, running_time_sum, running_count = None, 0, 0

for line in sys.stdin:
    key, value = line.split('\t')

    if last_key and last_key != key:
        print(last_key, str(round(running_time_sum / running_count)), sep='\t')
        last_key, running_time_sum, running_count = key, int(value), 1
    else:
        last_key, running_time_sum, running_count = key, running_time_sum + int(value), running_count + 1

if last_key:
    print(last_key, str(round(running_time_sum / running_count)), sep='\t')
