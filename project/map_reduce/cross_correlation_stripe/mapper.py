import sys


def pairing(src):
    result = list()

    for i in range(len(src)):
        for j in range(len(src)):
            if src[i] != src[j]:
                result.append([src[i], src[j]])

    return result


def collect_elements(pairs):
    collect = dict()

    for elem in pairs:
        key = elem[0]
        value = elem[1][1]

        if key[1] == value:
            continue

        if collect.get(key):
            collect.update({key: collect.get(key) + ',' + value})
        else:
            collect.update({key: value})

    return collect


def print_stripe(collect):
    values = dict()
    string = str()

    for elem in collect:

        for i in str(collect.get(elem)).split(','):
            if values.get(i):
                values.update({i: values.get(i) + 1})
            else:
                values.update({i: 1})
        for j in values:
            if string == '':
                string = (j + ':' + str(values.get(j)))
            else:
                string += (',' + j + ':' + str(values.get(j)))
        print(elem[1], string, sep='\t')
        values.clear()
        string = ''


def get_source():
    elem_id = 0
    temp = list()

    for line in sys.stdin:
        line = line.replace('\n', '')

        for token in line.split(' '):
            if token:
                temp.append((elem_id, token))
                elem_id += 1

        print_stripe(
            collect_elements(
                sorted(
                    pairing(
                        temp))))
        temp.clear()


if __name__ == '__main__':
    get_source()
