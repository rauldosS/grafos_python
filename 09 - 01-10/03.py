# -*- coding: utf-8 -*-
import networkx as nx

G = nx.Graph()
G.add_edge('A', 'B', weight=7)
G.add_edge('A', 'D', weight=5)
G.add_edge('B', 'C', weight=8)
G.add_edge('B', 'D', weight=9)
G.add_edge('B', 'E', weight=7)
G.add_edge('C', 'E', weight=5)
G.add_edge('D', 'E', weight=15)
G.add_edge('D', 'F', weight=6)
G.add_edge('E', 'F', weight=8)
G.add_edge('E', 'G', weight=9)
G.add_edge('F', 'G', weight=11)

posicoes = {
        'A': (0, 6),
        'B': (3, 4),
        'C': (6, 5),
        'D': (1, 2),
        'E': (5, 3),
        'F': (3, 1),
        'G': (6, 0)
    }


# rotulos = nx.get_edge_attributes(G, 'weight')
# nx.draw(G, posicoes, with_labels=True)
# nx.draw_networkx_edge_labels(G, posicoes, edge_labels=rotulos)

MST = nx.minimum_spanning_tree(G)
print(sorted(MST.edges(data=True)))
print("Custo total da MST:", MST.size(weight='weight'))
nx.draw_networkx(MST, posicoes, with_labels=True)