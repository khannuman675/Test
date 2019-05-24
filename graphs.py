import networkx as nx
import json

tabvar=[]
filename=input("Enter the Output file name: ")
filename+=".html"
f = open(filename, "a")

def returnNeighbours(graph,node,tabvar):
    neigbours= []
    
    for r,y in data.items():
        for i in  y:
            if i['id']==node:
                # class ='abc'
                # 'attrs': {'class':'abc', 'src':'/media/img/png', 'data-src':'custom data', 'method':'POST'}
                f.write('\t'*len(tabvar)+'<'+i['tag']+'>\n')
                tabvar.append('open')
                    
                    
    for n, nbrdict in graph.adjacency():
        if(str(n) ==  str(node)):
            for k,v in nbrdict.items():
                
                   
                    
                returnNeighbours(graph,k,tabvar)
    for r,y in data.items():
        for i in  y:
            if i['id']==node:
                tabvar.pop()
                f.write('\t'*len(tabvar)+'</'+i['tag']+'>\n')  
                            
                        
                #neigbours.append("<"+str(k)+">"+"</"+str(k)+">")
    # for r,y in data.items():
    #     for i in  y:
    #         if i['id']==node:
    #             print('\t'*len(tabvar),'</'+i['tag']+'>')  
            #return neigbours



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
#print(list(nx.edge_dfs(G)))
# ele = []
# array = []
# stack = []
# flag=0
# for x in list(nx.edge_dfs(G)):
#     flag=0
#     for j in stack:
#             if(str(j) == str(x[0])):
#                 flag=1
#     if(flag==0):
#         stack.append(x[0])
#         print(stack)
#         print("Checking for.."+str(x[0]))
#         for y in list(nx.edge_dfs(G)):
            
#             #print("1"+str(stack))
#             if(x[0]==y[0]):
#                 ele.append(y)
#                 #print("2"+str(stack))
            
#             #print("3"+str(stack))
#         array.append(ele)
#         ele = []
# print(array)

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
    
    returnNeighbours(G,n,tabvar)
    
    
   
    break
f.close()


  
