# -*- coding: utf-8 -*-
"""
Todos estão ligados entre si
"""

import networkx as nx

K = nx.complete_graph(30)
# pos = nx.circular_layout(K)

# nx.draw(K, pos, with_labels=True, node_color='g')

# nx.draw_circular(K)
# nx.draw_spring(K)
nx.draw_random(K)
