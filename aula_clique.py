import networkx as nx

G = nx.Graph()
G.add_edges_from({
        ('a', 'b'), ('a', 'c'), ('a', 'd'), 
        ('b', 'c'), ('b', 'd'), 
        ('c', 'e'), ('d', 'e'), 
    })

nx.draw_networkx(G)

print(nx.enumerate_all_cliques(G))