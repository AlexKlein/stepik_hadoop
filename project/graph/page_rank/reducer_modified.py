import sys


def get_random_move(nodes_pr):
    alpha = 0.1
    nodes_count = 5
    for node in nodes_pr:
        nodes_pr.update(
            {
                node:
                    str(
                        round(
                            alpha * (1 / nodes_count) + (1 - alpha) * float(nodes_pr.get(node))
                            , 3)
                    ).ljust(5, '0')
            }
        )

    return nodes_pr


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

    nodes_pr = get_random_move(nodes_pr)
    print_elements(nodes_pr, nodes_links)


if __name__ == '__main__':
    get_source()
