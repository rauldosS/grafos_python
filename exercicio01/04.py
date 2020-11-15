# -*- coding: utf-8 -*-
import networkx as nx

G = nx.Graph()
# Exercício 1
G.add_edge('A', 'B', weight=42)
G.add_edge('B', 'C', weight=42)
G.add_edge('C', 'D', weight=42)
G.add_edge('A', 'C', weight=42)
G.add_edge('D', 'A', weight=42)
G.add_edge('C', 'D', weight=42)

nx.draw(G, with_labels=True)

print("É Euleriano?", nx.is_eulerian(G))
print("É semi-Euleriano?", nx.is_semieulerian(G))
print("É não-Euleriano?", nx.is_semieulerian(G))

