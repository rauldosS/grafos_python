import networkx as nx
import matplotlib.pyplot as plt
from networkx.drawing.nx_pydot import graphviz_layout

G = nx.Graph()

G.add_edges_from([
        ('a', 'b'), ('a', 'c'),
        ('b', 'd'), ('b', 'e'),
        ('c', 'f'), ('c', 'g'),
        ('d', 'h'), ('d', 'i'),
        ('e', 'j'), ('e', 'k'),
        ('f', 'l'), ('f', 'm'),
        ('g', 'n'), ('g', 'o'),
    ])

print(nx.info(G))

print('|nAresta com BFS')
print(list(nx.bfs_edges(G, 'a')))

print('|Árvore BFS')
print(list(nx.bfs_tree(G, 'a')))

plt.title('Árvore')
#pos = graphviz_layout(G, prog="dot")
#nx.draw(G, pos=pos, with_labels=True)
plt.show()