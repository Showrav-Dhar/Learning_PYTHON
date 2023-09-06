book = {}
book['tom'] = {
    'name': 'tom',
    'address': 'jamal khan',
    'phone': '0198873773'
},
book['dip'] = {
    'name': 'dip',
    'address': 'Cheragi Pahar',
    'phone': '0193373773'
}

import json

# s = json.dumps(book) # json takes book dictionary as input and dumping it as a string so it will be in json format
# with open('myfile1213.txt','w') as f:
#     f.write(s)

with open('myfile1213.txt', 'r') as f:
    s = f.read()
    # print(s)
    book1 = json.loads(s)
    # print(book1['dip']['name'])
    for person in book1:
        print(book1[person])
