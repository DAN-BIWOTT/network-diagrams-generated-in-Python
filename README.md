# Network Giagrams Generated In Python
## Degree Centrality :
This is based on the assumption that important nodes have many connections.
## Closeness Centrality :
This is based on the assumption that important nodes are close to other nodes. It is calculated as the sum of the path lengths from the given node to all other nodes.
##Betweenness Centrality :
It assumes that important nodes connect other nodes. The formula for calculating Betweenness Centrality is as follows:
```Centrality_{betweenness}(v) = \Sigma_{s, t \epsilon N}(\sigma_{s, t}(v)/\sigma_{s, t}) ```
where `\sigma_{s, t}` is the number of shortest paths between nodes s and t. \sigma_{s, t}(v) is the number of shortest paths between nodes s and t that pass through v.
We may or may not include node v itself for the calculation.
# Running The Code
Do this on any of the files
```python centrality_by_company_labor.py```
# This is what you should see when you run the files
![file 1](network-diagrams-generated-in-Python/sample_results/image(1).png)
