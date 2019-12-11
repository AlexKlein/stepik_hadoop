import sys


def get_source():
    unique_id = 0
    query = dict()
    url = dict()

    for line in sys.stdin:
        line = line.replace('\n', '')
        key, value = line.split('\t')

        if str(value).find('query') != -1:
            query.update({(unique_id, key): str(value).replace('query:', '')})
        else:
            url.update({(unique_id, key): str(value).replace('url:', '')})

        unique_id += 1

    return query, url


def print_all():
    query, url = get_source()

    for q in sorted(query):
        for u in sorted(url):
            if q[1] == u[1]:
                print(q[1], query.get(q), url.get(u), sep='\t')


if __name__ == '__main__':
    print_all()
