import networkx as nx

G = nx.DiGraph()

G.add_weighted_edges_from([
        ('A', 'B', -1), ('A', 'C', 4), 
        ('B', 'C', 3), ('B', 'D', 2), ('B', 'E', 2), 
        ('D', 'B', 1), ('D', 'C', 5), 
        ('E', 'D', -3),
    ])

posicoes = {
        'A': (0, 1),
        'B': (2, 2),
        'C': (1, 0),
        'D': (3, 0),
        'E': (4, 1),
    }

rotulos = nx.get_edge_attributes(G, 'weight')

print('Caminho de A até E:', nx.bellman_ford_path(G, 'A', 'E'))
print('Distância de A até E:', nx.bellman_ford_path_length(G, 'A', 'E'))

caminhos = nx.single_source_bellman_ford_path(G, 'A')
distancias = nx.single_source_bellman_ford_path_length(G, 'A')

print("\nCaminhos a partir do nodo 'A'")
for c, d in zip(caminhos.values(), distancias.values()):
    print(f'Caminho de A até {c[-1]:}', c, 'Distância:', d)
    
nx.draw(G, posicoes, with_labels=True, connectionstyle='arc3, rad=0.1')
nx.draw_networkx_edge_labels(G, posicoes, edge_labels=rotulos, label_pos=0.3)