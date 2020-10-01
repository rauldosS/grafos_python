import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()
G.add_edges_from([
        ('1', '2'), ('1', '5'), 
        ('2', '3'), ('2', '6'), 
        ('3', '7'), 
        ('5', '7'),
    ])

plt.figure(1)
nx.draw_networkx(G)

print('É conectado?', 'Sim' if nx.is_connected(G) else 'Não')
print('# de componentes conexas (figura1):', nx.number_connected_components(G))
print('Componentes conexa:', list(nx.connected_components(G)))

H = nx.Graph()
H.add_edges_from([
        ('1', '3'), ('1', '5'), 
        ('2', '6'), 
        ('3', '7'), 
        ('5', '7'),
    ])

plt.figure(2)
nx.draw_networkx(H)

print('É conectado?', 'Sim' if nx.is_connected(H) else 'Não')
print('# de componentes conexas (figura2):', nx.number_connected_components(H))
print('Componentes conexa:', list(nx.connected_components(H)))