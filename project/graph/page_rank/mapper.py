import sys


def get_source():
    for line in sys.stdin:
        line = line.replace('\n', '')
        node, page_rank, nodes_to = line.split('\t')
        print(node, page_rank, nodes_to, sep='\t')
        nodes_to = nodes_to.replace('{', '').replace('}', '')
        counter = nodes_to.count(',') + 1

        for node_to in nodes_to.split(','):
            print(node_to, str(round(float(page_rank) / int(counter), 3)).ljust(5, '0'), '{}', sep='\t')


if __name__ == '__main__':
    get_source()
