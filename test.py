import json
data={}
data['tag'] = []  
data['tag'].append({  
    'id': 1,
    'tag': 'html',
    'child': [2,3]
})
data['tag'].append({  
    'id': 2,
    'tag': 'div',
    'child': []
})
data['tag'].append({  
    'id': 3,
    'tag': 'p',
    'child': []
})
with open('datajs.txt', 'w') as outfile:  
    json.dump(data, outfile)