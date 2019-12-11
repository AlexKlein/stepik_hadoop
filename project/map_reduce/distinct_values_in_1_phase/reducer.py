import sys


count = 0
last_token = None
result = dict()
temp = dict()

for line in sys.stdin:
    line = line.replace('\n', '')
    (value, key) = line.split('\t')
    token = (value, key)

    if token and token != last_token:
        if temp.get(token):
            count += 1
            last_token = token
        else:
            temp.update({token: count})

for elem in temp:
    if result.get(elem[1]):
        result.update({elem[1]: result.get(elem[1]) + 1})
    else:
        result.update({elem[1]: 1})

for key in result:
    print(key, result[key], sep='\t')
