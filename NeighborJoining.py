from Bio import Phylo
from io import StringIO
from Table import printTable

def algo(leaves, pairwise_dist, graph):
    
    length = len(leaves)

    if length == 2:
        node_1 = leaves[0]
        node_2 = leaves[1]
        new_node = node_1 + node_2
        print(f'Join last 2 nodes {node_1} and {node_2}')
        print()
        graph[new_node] = {node_1:pairwise_dist[0][1]/2, node_2:pairwise_dist[1][0]/2}
        return ([], pairwise_dist, graph)
    

    Ri = {}
    for i, l in enumerate(leaves):
        Ri[l] = (1/(length-2)) * sum(pairwise_dist[i])
        print(f'r{leaves[i]} = {(1/(length-2))} * ({"+".join(list(map(lambda x: str(x), pairwise_dist[i])))}) = {Ri[l]}')
    print()

    lowest_d = float('inf')
    lowest_pos = (None, None)
    divergence_matrix = [[0 for j in range(length)] for i in range(length)]
    for i in range(length):
        for j in range(length):
            if leaves[i] == leaves[j]:
                divergence_matrix[i][j] = 0
            else:
                new_d = pairwise_dist[i][j] - Ri[leaves[i]] - Ri[leaves[j]]
                if new_d < lowest_d:
                    lowest_d = new_d
                    lowest_pos = (i, j)
                print(f'M({leaves[i]}{leaves[j]}) = {pairwise_dist[i][j]} - {Ri[leaves[i]]} - {Ri[leaves[j]]} = {new_d}') if i <= j else 1
                divergence_matrix[i][j] = new_d
    print()

    x, y = lowest_pos
    node_1 = leaves[x]
    node_2 = leaves[y]
    new_node = node_1 + node_2
    print(f'Choose node {node_1} and {node_2} to form {new_node}')
    print()
    
    new_d_1 = 0.5*(pairwise_dist[x][y]+Ri[node_1]-Ri[node_2])
    new_d_2 = 0.5*(pairwise_dist[x][y]+Ri[node_2]-Ri[node_1])
    graph[new_node] = {node_1:new_d_1, node_2:new_d_2}
    print(f'W({new_node},{node_1}) = 0.5*({pairwise_dist[x][y]} + {Ri[node_1]} - {Ri[node_2]}) = {new_d_1}')
    print(f'W({new_node},{node_2}) = 0.5*({pairwise_dist[x][y]} + {Ri[node_2]} - {Ri[node_1]}) = {new_d_2}')
    print()

    new_leaves = leaves.copy()
    new_leaves.remove(node_1)
    new_leaves.remove(node_2)
    new_leaves.append(new_node)

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
        new_d = 0.5 * (pairwise_dist[i][x] + pairwise_dist[i][y] - pairwise_dist[x][y])
        print(f'd({leaves[i]}, {new_node}) = 0.5*({pairwise_dist[i][x]} + {pairwise_dist[i][y]} - {pairwise_dist[x][y]}) = {new_d}')
        temp_row.append(new_d)
        new_dist.append(temp_row)
    new_dist.append(([None]*(new_length-1)) + [0])
    for i in range(new_length-1):
        for j in range(new_length):
            new_dist[j][i] = new_dist[i][j]

    print()
    printTable(new_leaves, new_leaves, new_dist, 10)

    return (new_leaves, new_dist, graph)

def neighborJoining(leaves, pairwise_dist):

    original_length = len(leaves)

    printTable(leaves, leaves, pairwise_dist, 10)
    print()

    graph = {}

    while len(leaves) != 0:
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
