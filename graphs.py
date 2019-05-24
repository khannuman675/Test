import networkx as nx
import json


def returnNeighbours(graph,node):
    neigbours= []
    for n, nbrdict in graph.adjacency():
        if(str(n) ==  str(node)):
            for k,v in nbrdict.items():
                neigbours.append("<"+str(k)+">"+"</"+str(k)+">")
            return neigbours



with open('jsondata.txt') as json_file:  
    data = json.load(json_file)
G = nx.DiGraph()
for k,v in data.items():
    for i in  v:
       # print(i)
        G.add_node(i['id'])
        n=i['id']
        for x in i['child']:
            G.add_weighted_edges_from([(n,x,1)])
print(list(nx.edge_dfs(G)))
ele = []
array = []
stack = []
flag=0
for x in list(nx.edge_dfs(G)):
    flag=0
    for j in stack:
            if(str(j) == str(x[0])):
                flag=1
    if(flag==0):
        stack.append(x[0])
        print(stack)
        print("Checking for.."+str(x[0]))
        for y in list(nx.edge_dfs(G)):
            
            #print("1"+str(stack))
            if(x[0]==y[0]):
                ele.append(y)
                #print("2"+str(stack))
            
            #print("3"+str(stack))
        array.append(ele)
        ele = []
print(array)

# newdict={}

# for x in array:
#     print(x)
#     for y in x:
#         newdict[y[0]]=x

# print(newdict)
# #newdict1=
# for w in array:
#     for q in w:
#         if q[1] in newdict.keys():
#             q[1]=newdict[q[1]]
    



for n in G.nodes():
    print(str(n)+"\n"+str(returnNeighbours(G,n)))



  
# function for adding edge to graph 

# def addEdge(graph,u,v): 
#     graph[u].append(v) 
  
# # definition of function 
# def generate_edges(graph): 
#     edges = [] 
  
#     # for each node in graph 
#     for node in graph: 
          
#         # for each neighbour node of a single node 
#         for neighbour in graph[node]: 
              
#             # if edge exists then append 
#             edges.append((node, neighbour)) 
#     return edges 
  
# # declaration of graph as dictionary 
# addEdge(graph,'a','c') 
# addEdge(graph,'b','c') 
# addEdge(graph,'b','e') 
# addEdge(graph,'c','d') 
# addEdge(graph,'c','e') 
# addEdge(graph,'c','a') 
# addEdge(graph,'c','b') 
# addEdge(graph,'e','b') 
# addEdge(graph,'d','c') 
# addEdge(graph,'e','c') 
  
# # Driver Function call  
# # to print generated graph 
# print(generate_edges(graph)) 

        