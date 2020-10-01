import networkx as nx

G = nx.Graph()
G.add_edges_from([
        (1, 2), (1, 4),
        (2, 3), (2, 8),
        (3, 4), (3, 6),
        (4, 5),
        (5, 6), (5, 7),
        (6, 7),
        (7, 8), (7, 9),
        (8, 9)
    ])

posicoes = {
        1: (0, 0),
        2: (1, 0),
        3: (1, 1),
        4: (1, 2),
        5: (2, 2),
        6: (2, 1),
        7: (3, 1),
        8: (3, 0),
        9: (4, 0),
    }

print("É Euleriano?", nx.is_eulerian(G))
print("Arestas:", G.edges())

G_eulerizado = nx.eulerize(G)
print("\n Euleriano?", nx.is_eulerian(G_eulerizado))
print("Arestas:", G_eulerizado.edges())

nx.draw_networkx(G, pos=posicoes)