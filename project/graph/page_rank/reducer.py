import sys


def print_elements(nodes_pr, nodes_links):
    for node in nodes_links:
        print(node, nodes_pr.get(node, '0.000'), nodes_links.get(node), sep='\t')


def get_source():
    nodes_pr = dict()
    nodes_links = dict()

    for line in sys.stdin:
        line = line.replace('\n', '')
        node, page_rank, nodes_to = line.split('\t')

        if (node in nodes_pr) and (nodes_to == '{}'):
            nodes_pr.update({node: str(round(float(page_rank) + float(nodes_pr.get(node)), 3)).ljust(5, '0')})
        elif (node not in nodes_pr) and (nodes_to == '{}'):
            nodes_pr.update({node: page_rank})

        if nodes_to != '{}':
            nodes_links.update({node: nodes_to})

    print_elements(nodes_pr, nodes_links)


if __name__ == '__main__':
    get_source()
