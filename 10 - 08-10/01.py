import networkx as nx

G = nx.DiGraph([
        (1, 4), (1, 5), (1, 7),
        (2, 3), (2, 5), (2, 6),
        (3, 4), (3, 5),
        (5, 6),
        (6, 7)
    ])

A = nx.adjacency_matrix(G)
print(A.todense())

print(list(nx.topological_sort(G)))
print(list(nx.all_topological_sorts(G)))
print(len(list(nx.all_topological_sorts(G))))
print(nx.is_directed_acyclic_graph(G))