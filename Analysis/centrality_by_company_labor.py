import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt

#read columns from file then add into adges
df = pd.read_excel('../dataset/TESCO_PLC.xlsx',sheet_name='Attributes')
sub = df.to_numpy()
# print(sub[2][0])
# print(df['Subsidiary name'].shape)
G_symmetric = nx.Graph()
for x in sub:
   G_symmetric.add_edge(x[0],x[1])
#    print("Degree of this country node "+ x[1] + " " + str(nx.degree(G_symmetric,x[1])))#Degree of a node defines the number of connections
#    print("Closeness Centrality of this country node "+ x[1] + " " + str(nx.closeness_centrality(G_symmetric)))#Degree of a node defines the number of connections
   xAxis= nx.degree(G_symmetric,x[1])
   yAxis= nx.closeness_centrality(G_symmetric)
   plt.scatter(x[0], x[3], c=20, vmin=0, vmax=20, s=35, cmap = plt.cm.plasma)

nodes = nx.draw_networkx(G_symmetric)
plt.colorbar(nodes)
plt.show()
print("done")