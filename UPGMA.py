from Bio import Phylo
from io import StringIO
from Table import printTable

def algo(leaves, pairwise_dist, graph):
    
    length = len(leaves)

    lowest_dist = float('inf')
    lowest_pos = (None, None)
    for i in range(length):
        for j in range(length):
            if pairwise_dist[i][j] < lowest_dist and pairwise_dist[i][j] != 0:
                lowest_dist = pairwise_dist[i][j]
                lowest_pos = (i, j)

    x, y = lowest_pos
    node_1 = leaves[x]
    node_2 = leaves[y]
    new_node = node_1 + node_2
    print(f'Choose node {node_1} and {node_2} to form {new_node}')

    new_leaves = leaves.copy()
    new_leaves.remove(node_1)
    new_leaves.remove(node_2)
    new_leaves.append(new_node)

    def distToLeaf(graph, node):
        one, two = graph[node].items()
        if one[0] not in graph:
            return one[1]
        if node in graph:
            one, two = graph[node].items()
            return one[1] + distToLeaf(graph, two[0])

    if len(node_1) == 1 and len(node_2) == 1:
        graph[new_node] = {node_1: lowest_dist/2, node_2: lowest_dist/2}

    elif len(node_1) != 1 and len(node_2) == 1:
        one, two = graph[node_1].items()
        graph[new_node] = {node_1: (lowest_dist/2) - distToLeaf(graph, node_1), node_2: lowest_dist/2}

    elif len(node_1) == 1 and len(node_2) != 1:
        one, two = graph[node_2].items()
        graph[new_node] = {node_1: lowest_dist/2, node_2: (lowest_dist/2) - distToLeaf(graph, node_2)}

    else:
        one, two = graph[node_1].items()
        three, four = graph[node_2].items()
        graph[new_node] = {node_1: (lowest_dist/2) - distToLeaf(graph, node_1), node_2: (lowest_dist/2) - distToLeaf(graph, node_2)}

    new_length = len(new_leaves)
    new_dist = []
    for i in range(length):
        if i == x or i == y:
            continue
        temp_row = []
        for j in range(length):
            if j == x or j == y:
                continue
            temp_row.append(pairwise_dist[i][j])
        new_d = round((pairwise_dist[i][x] * len(leaves[x])  + pairwise_dist[i][y] * len(leaves[y])) / (len(leaves[x]) + len(leaves[y])), 3)
        print(f'dist({leaves[i]}, {new_node}) = {pairwise_dist[i][x]}*{len(leaves[x])} + {pairwise_dist[i][y]}*{len(leaves[y])} / {(len(leaves[x]) + len(leaves[y]))} = {new_d}')
        temp_row.append(new_d)
        new_dist.append(temp_row)
    new_dist.append(([None]*(new_length-1)) + [0])
    for i in range(new_length-1):
        for j in range(new_length):
            new_dist[j][i] = new_dist[i][j]

    print()
    printTable(new_leaves, new_leaves, new_dist, 10)

    return (new_leaves, new_dist, graph)

def upgma(leaves, pairwise_dist):

    original_length = len(leaves)

    printTable(leaves, leaves, pairwise_dist, 10)
    print()

    graph = {}

    while len(leaves) != 1:
        leaves, pairwise_dist, graph = algo(leaves, pairwise_dist, graph)
        print()

    root = ''
    for k, v in graph.items():
        if len(k) == original_length:
            root = k
    
    def recursveGraph(root, graph):
        child_1, child_2 = graph[root].items()
        if len(child_1[0]) == 1 and len(child_2[0]) == 1:
            return f'({child_1[0]}:{child_1[1]},{child_2[0]}:{child_2[1]})'
        elif len(child_1[0]) != 1 and len(child_2[0]) == 1:
            return f'{child_1[0]}:{child_1[1]}({recursveGraph(child_1[0], graph)}),{child_2[0]}:{child_2[1]})'
        elif len(child_1[0]) == 1 and len(child_2[0]) != 1:
            return f'({child_1[0]}:{child_1[1]},{child_2[0]}:{child_2[1]}({recursveGraph(child_2[0], graph)}))'
        else:
            return root + '(' + f'({child_1[0]}:{child_1[1]}' + recursveGraph(child_1[0], graph) + '),' + f'({child_2[0]}:{child_2[1]}' + recursveGraph(child_2[0], graph) + '))'
    
    handle = StringIO(recursveGraph(root, graph))
    tree = Phylo.read(handle, "newick")
    Phylo.draw(tree, branch_labels=lambda c: c.branch_length)
