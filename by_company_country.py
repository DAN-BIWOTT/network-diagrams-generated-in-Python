import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt

#read columns from file then add into adges
df = pd.read_excel('./dataset/TESCO_PLC.xlsx',sheet_name='Attributes')
sub = df.to_numpy()
# print(sub[2][0])
# print(df['Subsidiary name'].shape)
G_symmetric = nx.Graph()
for x in sub:
#    print(x[0])
#    print(x[1])
   G_symmetric.add_edge(x[0],x[1])
   print("Degree of this country node "+ x[1] + " " + str(nx.degree(G_symmetric,x[1])))#Degree of a node defines the number of connections

nx.draw_networkx(G_symmetric)
plt.show()
print("done")