# -*- coding: utf-8 -*-

import collections

def visita(n):
    print(n)
    
# Algoritmo interativo
# Busca em largura (BFS - Breadth First Search)

def bfs(grafo, inicio, objetivo=[]):
    # Mantém registro dos nodos já visitados
    visitados = set()
    
    # Fila (deque) de nodos a serem visitados
    fila = collections.deque([inicio])
    
    # Itera até que todos os nodos tenham sido verificados
    while fila:
        # Retira o primeiro elemento da fila
        nodo = fila.popleft()
        
        if nodo not in visitados:
            visita(nodo)
            
            # Adiciona nodo ao conjunto dos já visitados
            visitados.add(nodo)
            
            if nodo in objetivo:
                break
            
            vizinhos = grafo[nodo]
            
            # Adiciona os vizinhos ao final da fila
            for vizinho in vizinhos:
                fila.appendleft(vizinho) 
                
    return visitados
                

if __name__=='__main__':
    grafo = {
            'A': ['B', 'C'],
            'B': ['D', 'E'],
            'C': ['F', 'G'],
            'D': ['H', 'I'],
            'E': ['J', 'K'],
            'F': ['L', 'M'],
            'G': ['N', 'O'],
            'H': [],
            'I': [],
            'J': [],
            'K': [],
            'L': [],
            'M': [],
            'N': [],
            'O': [],
        }
    
    bfs(grafo, 'A', ['C', 'L'])