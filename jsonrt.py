import json

with open('data.txt') as json_file:  
    data = json.load(json_file)
    for p in data['people']:
        print('Name: ' + p['name'])
        print('Age :' + p['age'])
        print('City: ' + p['city'])
        print('')

        
x={"people": [{"name": "Scott", "age": 24, "city": "Mumbai"},
 		{"name  ": "Larry", "age":34, "city": "Pune"},
		 {"name": "Tim", "age": 31, "city": "Nashik"}]}
for p in x['people']:
    print('Name: ' + p['name'])
    print('Age :' + str(p['age']))
    print('City: ' + p['city'])
    print('')