# s = input()
#
#
# isAlnum = any((char.isalnum() for char in s))
# isAlpha = any((char.isalpha() for char in s))
# isdigit = any((char.isdigit() for char in s))
# isLower = any((char.islower() for char in s))
# isUpper = any((char.isupper() for char in s))
#
# print(isAlnum)
# print(isAlpha)
# print(isdigit)
# print(isLower)
# print(isUpper))

#
# book = {'dip':1,'antu':2,'richi':3}
# for i in book:
#     print(book[i])

#Reading a file
# f = open('myfile1213.txt','r')
# text = f.read()
# print(text)
# f.close()

# f = open('myfile1213v2','w')
# f.write("Hello how are you doing")
# f = open('myfile1213v2','r')
# text = f.read()
# print(text)

# f = open('myfile1213.txt','w')
# f.write('Hey SHowrav How was your day?')
#
# f = open('myfile1213.txt','r')
# text = f.read()
# print(text)
#
#
# f = open('myfile1213.txt','a')
# f.write('Work Hard and keep patitent your time will come')
# f.close()


# with() method
#
# with open('myfile1213.txt','w') as f:
#     f.write('')

#working with json file in python
infoBook = {}

infoBook['dip'] = {
    'name' : 'dip',
    'age'  : '23',
    'gender': 'male'
},
infoBook['antu']= {
    'name' : 'antu',
    'age'  : '28',
    'gender': 'male'
}
import json
# s = json.dumps(infoBook)
# with open('myfile1213.txt','w') as f:
#     f.write(s)

with open('myfile1213.txt','r') as f :
    s = f.read()
    infoBook1 = json.loads(s)

    for person in infoBook1:
        print(infoBook1[person])