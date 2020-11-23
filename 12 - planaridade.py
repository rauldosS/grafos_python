import networkx as nx
import matplotlib.pyplot as plt
G1 = nx.Graph()
G1.add_edges_from([
 ('a', 'c'), ('a', 'd'), ('a', 'e'), ('a', 'f'), ('a', 'g'),
 ('a', 'h'), ('a', 'i'), ('a', 'j'), ('a', 'k'), ('a', 'l'),
 ('b', 'c'), ('b', 'd'), ('b', 'e'), ('b', 'f'), ('b', 'g'),
 ('b', 'h'), ('b', 'i'), ('b', 'j'), ('b', 'k'), ('b', 'l'),
 ])
posicoes1 = {
 'a': (0, 6.5), 'b': (0, 2.5),
 'c': (1, 9), 'd': (1, 8),
 'e': (1, 7), 'f': (1, 6),
 'g': (1, 5), 'h': (1, 4),
 'i': (1, 3), 'j': (1, 2),
 'k': (1, 1), 'l': (1, 0),
 }
G2 = nx.Graph()
G2.add_edges_from([
 ('a', 'd'), ('a', 'e'), ('a', 'f'),
 ('b', 'd'), ('b', 'e'), ('b', 'f'),
 ('c', 'd'), ('c', 'e'), ('c', 'f'),
 ])
posicoes2 = {
 'a': (0, 3), 'b': (0, 2),
 'c': (0, 1), 'd': (1, 3),
 'e': (1, 2), 'f': (1, 1)
 }
g1_planar = 'É planar' if nx.check_planarity(G1)[0] else 'Não é planar'
g2_planar = 'É planar' if nx.check_planarity(G2)[0] else 'Não é planar'
plt.figure(figsize=(4, 5), dpi=150)
nx.draw_networkx(G1, pos=posicoes1)
plt.text(0.15, 8.5, s=g1_planar, bbox=dict(facecolor='red', alpha=0.5),
horizontalalignment='center')
plt.show()
plt.figure(figsize=(4, 5), dpi=150)
plt.margins(y=.15)
nx.draw_networkx(G2, pos=posicoes2)
plt.text(0.15, 3.15, s=g2_planar, bbox=dict(facecolor='red', alpha=0.5),
horizontalalignment='center')
plt.ylim(bottom=.9, top=3.3)
plt.show()