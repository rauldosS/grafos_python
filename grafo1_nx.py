# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 21:29:05 2020

@author: Raul
"""

# Importa biblioteca networkx com o apelido de nx
import networkx as nx

# Criando um novo objeto de classe Grafo
g = nx.Graph()

#Acrescentando vértices (nodos) ao grafo
g.add_node(1)
g.add_nodes_from([2, 3])
print("Nodos (vértices):", g.nodes())

#Acrescentar as arestas = ligações (edges)
g.add_edge(1, 2)
aresta = (2, 3) #aresta[0], aresta[1]
g.add_edge(*aresta)
    
g.add_edges_from([(1, 3), (3, 2)])

print("Arestas (edges): ", g.edges())

nx.draw_networkx(g)