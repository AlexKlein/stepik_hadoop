import sys


def pairing(src):
    result = list()

    for i in range(len(src)):
        for j in range(len(src)):
            if src[i] != src[j]:
                result.append([src[i], src[j]])

    return result


def get_source():
    pairs = list()
    temp = list()

    for line in sys.stdin:
        line = line.replace('\n', '')

        for token in line.split(' '):
            if token:
                temp.append(token)

        pairs.append(pairing(temp))
        temp.clear()

    return pairs


if __name__ == '__main__':
    source = get_source()
    for elem in source:
        for sub_elem in elem:
            print(sub_elem[0] + ',' + sub_elem[1], 1, sep='\t')
