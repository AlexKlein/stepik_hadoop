import sys


last_key, running_time_sum, running_count = None, 0, 0

for line in sys.stdin:
    key, value_pair = line.split('\t')
    value_time, value_count = value_pair.split(';')

    if last_key and last_key != key:
        print(last_key, str(running_time_sum) + ';' + str(running_count), sep='\t')
        last_key, running_time_sum, running_count = key, int(value_time), 1
    else:
        last_key, running_time_sum, running_count = \
            key, running_time_sum + int(value_time), running_count + int(value_count)

if last_key:
    print(last_key, str(running_time_sum) + ';' + str(running_count), sep='\t')
