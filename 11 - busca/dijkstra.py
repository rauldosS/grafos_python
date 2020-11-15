import networkx as nx
import collections

G = nx.DiGraph()
G.add_weighted_edges_from([
        ('A', 'B', 20), ('A', 'D', 80), ('A', 'G', 90),
        ('B', 'F', 10),
        ('C', 'D', 10), ('C', 'F', 50), ('C', 'H', 20),
        ('D', 'C', 10), ('D', 'F', 40), ('D', 'G', 20),
        ('E', 'B', 50), ('E', 'G', 30),
        ('F', 'C', 10), ('F', 'D', 40),
        ('G', 'A', 20), ('G', 'D', 20),
    ])

posicoes = {
        'A': (1.5, 1.5),
        'B': (0, 2),
        'C': (2.2, 3.8),
        'D': (2.5, 1.8),
        'E': (0.3, 0),
        'F': (0.6, 4),
        'G': (2, .3),
        'H': (2.7, 3.5),
    }

caminhos = nx.single_source_dijkstra_path(G, 'A') # Todos os caminhos do A para todos os outros vértices
distancias = nx.single_source_dijkstra_path_length(G, 'A') # Distancias mais curtas para todos os vértices
caminhos_od = collections.OrderedDict(sorted(caminhos.items()))

print(caminhos_od)

print("\nCaminhos a partir do nodo 'A'")
for caminho in caminhos.values():
    distancia = distancias[caminho[-1]]
    print(f'Caminho de A até {caminho[-1]:}', caminho, 'Distância:', distancia)
    
rotulos = nx.get_edge_attributes(G, 'weight')
nx.draw(G, posicoes, with_labels=True, connectionstyle='arc3, rad=0.1')
nx.draw_networkx_edge_labels(G, posicoes, edge_labels=rotulos, label_pos=0.3)
