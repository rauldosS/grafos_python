# -*- coding: utf-8 -*-
import networkx as nx
G = nx.Graph()
G.add_edges_from([
 ('a', 'b'), ('a', 'd'),
 ('b', 'c'), ('b', 'e'),
 ('c', 'e'),
 ('d', 'f'), ('d', 'g')
 ])
posicoes = {
 'a': (0, 2), 'b': (1.5, 3),
 'c': (5, 2.5), 'd': (1, 1),
 'e': (3, 2), 'f': (0, 0),
 'g': (4, 0)
 }
print(nx.maximal_independent_set(G))
nx.draw_networkx(G, pos=posicoes)
