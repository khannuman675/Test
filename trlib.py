from treelib import Node, Tree
import json
with open('jsondata.txt') as json_file:  
    data = json.load(json_file)
tree = Tree()
tree.create_node(identifier='0',data='<html></html>')
#print(len(data["tag"]))
key={"sd"}
key.clear()
for k,v in data.items():
    for i in  v:
        _id = str(i['id'])
        _tag = str(i['tag'])
        parent=i['parent']
        for x in parent:
            tree.create_node(identifier=_id,parent=str(x),data=_tag)
tree.show()
#tree.show()
x=tree.to_json()
print(x)
tree.save2file('tree.txt',data_property=True)
# print(x)
# print(key)