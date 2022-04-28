from collections import defaultdict

def make_undirected_graph(edge_list):
    """ Makes an undirected graph from a list of edge tuples. """
    graph = defaultdict(set)
    for e in edge_list:
        graph[e[0]].add(e[1])
        graph[e[1]].add(e[0])
    return graph


def reachable(graph, start_node):
    """
    Returns:
      the set of nodes reachable from start_node
    """
    result = set([start_node])
    frontier = [start_node]
    while len(frontier) != 0:
        node = frontier.pop(0)
        result.add(node)
        for next in graph[node]:
            if next in result:
                continue
            frontier.append(next)
    return result

def test_reachable():
    graph = make_undirected_graph([('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'B')])
    assert sorted(reachable(graph, 'A')) == ['A', 'B', 'C', 'D']

    graph = make_undirected_graph([('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'B'), ('E', 'F'), ('F', 'G')])
    assert sorted(reachable(graph, 'A')) == ['A', 'B', 'C', 'D']
    assert sorted(reachable(graph, 'E')) == ['E', 'F', 'G']

test_reachable()


def connected(graph):
    ### TODO
    lst = list(graph.keys())
    res = reachable(graph,lst[0])
    for node in graph.keys():
        temp = reachable(graph, node)
        if temp != res:
            return False
        res = temp
    return True


def test_connected():
    graph = make_undirected_graph([('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'B')])
    assert connected(graph) == True
    graph = make_undirected_graph([('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'B'), ('E', 'F'), ('F', 'G')])
    assert connected(graph) == False

test_connected()

def n_components(graph):
    """
    Returns:
      the number of connected components in an undirected graph
    """
    ### TODO
    if connected(graph):
        return 1
    lst = list(graph.keys())
    first = list(reachable(graph,lst[0]))
    res = 1
    for node in graph.keys():
        if node in first:
            continue
        res += 1
        first += list(reachable(graph, node))
    return res
        

def test_n_components():
    graph = make_undirected_graph([('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'B')])
    assert n_components(graph) == 1

    graph = make_undirected_graph([('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'B'), ('E', 'F'), ('F', 'G')])
    assert n_components(graph) == 2

test_n_components()