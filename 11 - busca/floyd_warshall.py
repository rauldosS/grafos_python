import networkx as nx
import collections
import json

G = nx.DiGraph()
G.add_weighted_edges_from([
        ('A', 'B', 1), ('A', 'E', 1),
        ('B', 'C', 1), ('B', 'D', 2),
        ('C', 'D', 4), ('C', 'E', 2),
        ('D', 'A', 3),
        ('E', 'D', 1), ('E', 'A', 2),
    ])

posicoes = {
        'A': (0, 1),
        'B': (1.25, 1.75),
        'C': (2.5, 1),
        'D': (2, 0),
        'E': (.75, 0),
    }

predecessores, distancias = nx.floyd_warshall_predecessor_and_distance(G)
predecessores_od = collections.OrderedDict(sorted(predecessores.items()))
distancias_od = collections.OrderedDict(sorted(distancias.items()))

resultados_np = nx.floyd_warshall_numpy(G)
print(resultados_np)

print('\nDistâncias:')
for chave, valor in distancias_od.items():
    od = collections.OrderedDict(sorted(valor.items()))
    print(f'Distâncias a partir de {chave}:', json.dumps(od))
    
print("\nCamihos:")
for source, valor in predecessores_od.items():
    valor_od = collections.OrderedDict(sorted(valor.items()))
    for target, caminho in valor_od.items():
        print(f'Caminhos a partir de {source} até {target}')

nx.reconstruct_path(source, target, predecessores_od)

print("")

rotulos = nx.get_edge_attributes(G, 'weight')
nx.draw(G, posicoes, with_labels=True, connectionstyle='arc3, rad=0.1')
nx.draw_networkx_edge_labels(G, posicoes, edge_labels=rotulos, label_pos=0.3)