"""
Created on Sun Oct 11 14:06:26 2020
@author: Raul dos Santos Moraes
"""

import networkx as nx
import collections

G = nx.Graph()

G.add_edges_from([
        ('A', 'B'), ('A', 'F'), ('A', 'C'),
        ('B', 'G'), ('B', 'D'),
        ('C', 'H'), ('C', 'E'),
        ('D', 'B'), ('D', 'I'), ('D', 'E'),
        ('E', 'J'),
        ('F', 'I'), ('F', 'J'),
        ('G', 'H'), ('G', 'J'),
        ('H', 'I')
    ])

posicoes = {
        'A': (5, 10), #(coluna, linha)
        'B': (2, 7),
        'C': (8, 7),
        'D': (2.5, 2),
        'E': (7.5, 2),
        'F': (5, 8),
        'G': (3.5, 6),
        'H': (6.5, 6),
        'I': (4, 3),
        'J': (6, 3),
    }

nx.draw(G, posicoes, with_labels=True)

print('Diâmetro: ', nx.diameter(G))
print('Raio:', nx.radius(G))
print('Centro:', nx.center(G))

ex_ordenadas = sorted(nx.eccentricity(G).items())
print('Excentricidades:', dict(ex_ordenadas))

for vertice, excentricidade in ex_ordenadas:
    print(vertice, excentricidade)