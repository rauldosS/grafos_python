# -*- coding: utf-8 -*-
import networkx as nx

G = nx.Graph()
G.add_edge('A', 'B', weight=42)
G.add_edge('A', 'G', weight=45)
G.add_edge('B', 'C', weight=38)
G.add_edge('B', 'G', weight=35)
G.add_edge('C', 'D', weight=70)
G.add_edge('C', 'F', weight=28)
G.add_edge('D', 'E', weight=80)
G.add_edge('E', 'F', weight=62)
G.add_edge('F', 'G', weight=40)

posicoes = {
        'A': (0, 3),
        'B': (3, 2),
        'C': (6, 1),
        'D': (10, 0),
        'E': (9, 5),
        'F': (7, 3),
        'G': (2, 5)
    }


# rotulos = nx.get_edge_attributes(G, 'weight')
nx.draw(G, posicoes, with_labels=True)
# nx.draw_networkx_edge_labels(G, posicoes, edge_labels=rotulos)

print("É Euleriano?", nx.is_eulerian(G))
print("Arestas:", G.edges(data=True))
print("# de arestas:", G.number_of_edges())
print("Soma total dos pesos:", G.size(weight='weight'))

G_eulerizado = nx.eulerize(G)
print("\nÉ Euleriano?", nx.is_eulerian(G_eulerizado))
print("Arestas:", G_eulerizado.edges(data=True))
print("# de arestas:", G_eulerizado.number_of_edges())
print("Soma total dos pesos:", G_eulerizado.size(weight='weight'))