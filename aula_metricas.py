import networkx as nx
import collections

G = nx.Graph()

G.add_edges_from([
        ('C', 'A'), ('C', 'B'), ('C', 'D'), ('C', 'F'),
        ('F', 'E'), ('F', 'G'), ('F', 'H'), ('F', 'I'), ('F', 'J'),
        ('I', 'H'), ('I', 'L'), ('I', 'J'),
        ('L', 'K'), ('L', 'M'),
        ('B', 'E'), ('D', 'G'), ('E', 'H'), ('G', 'J'),
    ])

nx.draw_networkx(G)

print('Diâmetro: ', nx.diameter(G))
print('Raio:', nx.radius(G))
print('Centro:', nx.center(G))

ex_ordenadas = sorted(nx.eccentricity(G).items())
print('Excentricidades:', dict(ex_ordenadas))

for vertice, excentricidade in ex_ordenadas:
    print(vertice, excentricidade)