import sys


def collect_elements(dist, endpoints):
    for i in dist:
        print(i, dist.get(i), endpoints.get(i)[1], sep='\t')
        if endpoints.get(i)[1] != '{}':
            for j in endpoints.get(i)[1].replace('{', '').replace('}', '').split(','):
                try:
                    if dist.get(i) == 'INF':
                        print(j, dist.get(i), '{}', sep='\t')
                    else:
                        print(j, int(dist.get(i)) + 1, '{}', sep='\t')
                except TypeError:
                    if j in dist:
                        print(j, 0, '{}', sep='\t')
                    else:
                        if dist.get(i) == 'INF':
                            print(j, dist.get(i), '{}', sep='\t')
                        else:
                            print(j, int(dist.get(i)) + 1, '{}', sep='\t')


def get_source():
    counter = 0
    dist = dict()
    endpoints = dict()
    prev_steps = 0
    temp = set()

    for line in sys.stdin:
        line = line.replace('\n', '')
        node, distance_origin, nodes_to = line.split('\t')

        for elem in str(nodes_to).replace('{', '').replace('}', '').split(','):
            temp.add(elem)

        dist.update({node: distance_origin})

        if node in temp:
            for point in endpoints:
                if node in set(endpoints.get(point)[1]):
                    parent_node = point
                    prev_steps = dist.get(parent_node)

        if prev_steps == 'INF':
            endpoints.update({node: (prev_steps, nodes_to)})
        elif counter == 0:
            endpoints.update({node: (distance_origin, nodes_to)})
        else:
            endpoints.update({node: (int(prev_steps) + 1, nodes_to)})

        counter += 1

    collect_elements(dist, endpoints)


if __name__ == '__main__':
    get_source()