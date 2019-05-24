import json

data = {}  
data['people'] = []  
data['people'].append({  
    'name': 'Scott',
    'age': '45',
    'city': 'Mumbai'
})
data['people'].append({  
    'name': 'Larry',
    'age': '69',
    'city': 'Pune'
})
data['people'].append({  
    'name': 'Tim',
    'age': '39',
    'city': 'Nashik'
})

with open('data.txt', 'w') as outfile:  
    json.dump(data, outfile)