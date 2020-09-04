import networkx as nx
import numpy as np

# G = nx.complete_graph(5)
# nx.draw(G, with_labels=True)

# MA = nx.to_numpy_matrix(G)
# print(MA)

matriz = np.matrix  ([    #1  2  3 coluna
                          [0, 1, 1], #1 linha
                          [1, 0, 1], #2
                          [1, 1, 0], #3
                    ])

print(matriz[0, 2])
print(matriz[:, 2]) # Apenas (toda) a segunda coluna
print(matriz[0:2, 0:2]) # Submatriz

H = nx.from_numpy_matrix(matriz)
nx.draw(H, with_labels=True)