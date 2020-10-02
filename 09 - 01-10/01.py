# -*- coding: utf-8 -*-

import networkx as nx

G = nx.barbell_graph(10, 0)
nx.draw_networkx(G)
print(list(nx.bridges(G)))