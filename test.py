import networkx as nx
import matplotlib.pyplot as plt

g = nx.Graph()
g.add_edge(1, 2)
nx.draw_networkx(g)
plt.show()
