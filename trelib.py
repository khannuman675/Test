from treelib import Node, Tree
import types
import json
with open('datajs.txt') as json_file:  
    data = json.load(json_file)
tree = Tree()
tree.create_node("Haesfdhrry", "harry")  # root node
tree.create_node("Jane", "jane", parent="harry")
tree.create_node("Bill", "bill", parent="harry")
tree.create_node("Diane", "diane",parent="bill")
tree.create_node("Mary", "mary", parent="diane")
tree.create_node("Mark", "mark", parent="jane",data="saaddfh")
tree.create_node(identifier=1,parent="bill")
print(len(data["tag"]))
tree.show()
# "key={"ds"}
# key.clear()
# val=[]
# for k,v in data.items():
#     for i in  v:
#        # print(i)
#         for q,w in i.items():
#            print(q,w)
#            key.add(q)
#            val.append(w)
#         length=len(key)
#         for add in range(len(val)-1):
#             tree.create_node(identifier=val[add],parent="diane")
#             add+=1
#             print(val)

# print(key)
# print(val)

# # x=tree.to_json()
# # print(x)
# # y=tree.nodes["mark"]
# # print(y)
# x=tree.nodes
# for k,v in x.items():
#     print(k,v.data)
#     if isinstance(v.data,list):
#         y=v.data
#         print(y[0]+y[1])




   
#tree.show()
#print(key)
