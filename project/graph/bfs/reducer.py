import sys


def print_elements(endpoints):
    for node in endpoints:
        print(node, endpoints.get(node)[0], endpoints.get(node)[1], sep='\t')


def get_source():
    dist = dict()
    endpoints = dict()

    for line in sys.stdin:
        line = line.replace('\n', '')
        node, distance_origin, nodes_to = line.split('\t')
        if (node in dist) and \
                (distance_origin != 'INF') and \
                (int(distance_origin) < int(dist.get(node))):
            dist.update({node: distance_origin})
        elif node not in dist:
            dist.update({node: distance_origin})

        if (node in endpoints) and \
                (endpoints.get(node)[1] != '') and \
                (nodes_to != '{}'):
            endpoints.update({node: (dist.get(node), nodes_to)})
        elif (node in endpoints) and \
                (dist.get(node) != 'INF') and \
                (endpoints.get(node)[0] != 'INF') and \
                (int(dist.get(node)) < int(endpoints.get(node)[0])):
            endpoints.update({node: (dist.get(node), endpoints.get(node)[1])})
        elif node not in endpoints:
            endpoints.update({node: (dist.get(node), nodes_to)})

    print_elements(endpoints)


if __name__ == '__main__':
    get_source()
