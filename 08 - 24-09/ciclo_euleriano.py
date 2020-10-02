import networkx as nx

G = nx.Graph()
G.add_edges_from([
        (1, 2), (1, 3),
        (2, 3), (2, 4), (2, 6),
        (3, 4), (3, 5),
        (4, 5), (4, 6),
        (5, 6), (5, 7),
        (6, 7)
    ])

posicoes = {
        1: (.5, 1),
        2: (0, .75),
        3: (1, .75),
        4: (.5, .5),
        5: (1, .25),
        6: (0, .25),
        7: (.5, 0),
    }

nx.draw_networkx(G, pos=posicoes)
print("Grafo G")
print("-------")
print("É Euleriano?", "Sim" if nx.is_eulerian(G) else "Não")
print("É Semieuleriano?", "Sim" if nx.is_semieulerian(G) else "Não")
print("É Tem caminho Euliriano?", "Sim" if nx.has_eulerian_path(G) else "Não")