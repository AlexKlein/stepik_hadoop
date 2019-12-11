import sys


class Graph(object):
    """
    A simple undirected, weighted graph
    """

    def __init__(self):
        self.nodes = set()
        self.edges = {}
        self.distances = {}

    def add_node(self, value):
        self.nodes.add(value)

    def add_edge(self, from_node, to_node, distance):
        self._add_edge(from_node, to_node, distance)
        self._add_edge(to_node, from_node, distance)

    def _add_edge(self, from_node, to_node, distance):
        self.edges.setdefault(from_node, [])
        self.edges[from_node].append(to_node)
        self.distances[(from_node, to_node)] = distance


def get_source():
    edge_count = 0
    edge_weights = dict()
    line_count = 0
    node_count = 0
    node_set = set()
    node_finish = 0
    node_start = 0
    result = dict()

    for line in sys.stdin:
        line = line.replace('\n', '')

        if line_count == 0:
            node_count, edge_count = line.split(' ')
        else:
            try:
                node_from, node_to, weight = line.split(' ')
                edge_weights.update({(int(node_from), int(node_to)): int(weight)})
                node_set.add(int(node_from))
                node_set.add(int(node_to))
            except ValueError:
                node_start, node_finish = line.split(' ')

        line_count += 1

    result.update({'edge_weights': edge_weights})
    result.update({'node_set': node_set})
    result.update({'node_count': node_count})
    result.update({'edge_count': edge_count})
    result.update({'node_start': node_start})
    result.update({'node_finish': node_finish})

    return result


def dijkstra(graph, initial_node):
    visited = {initial_node: 0}
    path = {}
    nodes = set(graph.nodes)

    while nodes:
        min_node = None
        for node in nodes:
            if node in visited:
                if min_node is None:
                    min_node = node
                elif visited[node] < visited[min_node]:
                    min_node = node

        if min_node is None:
            break

        nodes.remove(min_node)
        cur_wt = visited[min_node]

        for edge in graph.edges[min_node]:
            wt = cur_wt + graph.distances[(min_node, edge)]
            if edge not in visited or wt < visited[edge]:
                visited[edge] = wt
                path[edge] = min_node

    return visited, path


def shortest_path(graph, initial_node, goal_node):
    distances, paths = dijkstra(graph, initial_node)
    route = [goal_node]

    while goal_node != initial_node:
        route.append(paths[goal_node])
        goal_node = paths[goal_node]

    route.reverse()
    return route


def node_check(data):
    node_set = data.get('node_set')
    node_start = data.get('node_start')
    node_finish = data.get('node_finish')

    if (int(node_start) in node_set) and (int(node_finish) in node_set):
        return 0
    else:
        return -1


def count_distance(path, edge_weights):
    summarize = 0

    for i in range(len(path)):
        try:
            node_first = path[i]
            node_second = path[i + 1]
            summarize += edge_weights.get((node_first, node_second))
        except IndexError:
            break

    return summarize


if __name__ == '__main__':
    source = get_source()
    error = node_check(source)

    if error == -1:
        print(error)
        sys.exit(0)

    g = Graph()
    g.nodes = set(range(1, int(source.get('node_count')) + 1))

    for r in source.get('edge_weights'):
        g.add_edge(r[0], r[1], source.get('edge_weights').get(r))

    try:
        shortest_path = shortest_path(g, int(source.get('node_start')), int(source.get('node_finish')))
    except KeyError:
        error = -1
        print(error)
        sys.exit(0)

    print(count_distance(shortest_path, source.get('edge_weights')))
