# -*- coding: utf-8 -*-
import networkx as nx

G = nx.DiGraph()

G.add_node(1)
G.add_node(2)
G.add_node(3)
G.add_node(4)
G.add_node(5)

G.add_edge(1, 2)
G.add_edge(2, 3)
G.add_edge(3, 1)
G.add_edge(4, 5)
G.add_edge(5, 4)
G.add_edge(4, 6)
G.add_edge(6, 5)

nx.draw(G, with_labels=True)