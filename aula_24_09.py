import networkx as nx

G = nx.DiGraph()
G.add_edges_from([
        (1, 4),
        (2, 1), (2, 5), (2, 6),
        (3, 2), (3, 4),
        (4, 5),
        (5, 4),
        (6,3), (6,5),
        (7, 8)
    ])

# Dictionary: {chave: valor}
posicoes = {
        1: (1.5, .5),
        2: (1, 1),
        3: (2, 2),
        4: (2, 0),
        5: (0, 0),
        6: (0, 2),
        7: (.5, 1),
        8: (.5, .75)
    }
# nx.draw_networkx(G, pos=posicoes)

print("Componentes fracamente conexas")
print("---------------------------------------------------------------------")
print("Grafo 'G' é fracamente (simplesmente) conexo?",
      "Sim" if nx.is_weakly_connected(G) else "Não")
print("Componente fracamente conexas:", list(nx.weakly_connected_components(G)))

print("\nGrafo semiconexo")
print("---------------------------------------------------------------------")
print("Grafo 'G' é semiconexo (semi-fortemente conexo)?",
      "Sim" if nx.is_semiconnected(G) else "Não")

print("\nGrafo fortemente conexo")
print("---------------------------------------------------------------------")
print("Grafo 'G' é fortemente conexo?",
      "Sim" if nx.is_semiconnected(G) else "Não")
print("# de componentes fortemente conexas:",
      nx.number_strongly_connected_components(G))
print("Componentes fortemente conexas:",
      list(nx.strongly_connected_components(G)))
print("Maior componente conexa:",
      max(nx.strongly_connected_components(G), key=len))

grafo_reduzido = nx.condensation(G)
print("Grafo reduzido:", grafo_reduzido.nodes())
nx.draw_networkx(grafo_reduzido)
mapa = grafo_reduzido.graph['mapping']

rotulos = {}
for chave, valor in mapa.items():
    rotulos.setdefault(valor, []).append(chave)
print(rotulos)

nx.draw_networkx(grafo_reduzido, with_labels=True, labels=rotulos)