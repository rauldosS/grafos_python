import networkx as nx

G = nx.Graph()

G.add_node(1) 
G.add_node(2) 
G.add_node(3) 
G.add_node(4) 
G.add_node(5) 

print('Vértices:', G.nodes())


G.add_edge(1, 2)
G.add_edge(2, 3)
G.add_edge(3, 4)
G.add_edge(4, 5)
G.add_edge(5, 1)

print('Arestas:', G.edges())

nx.draw(G, with_labels=True, node_color='b')