# book = {}
# book['tom'] = {
#     'name': 'tom',
#     'address': 'jamal khan',
#     'phone': '0198873773'
# },
# book['dip'] = {
#     'name': 'dip',
#     'address': 'Cheragi Pahar',
#     'phone': '0193373773'
# }
#
# import json
#
# # s = json.dumps(book) # json takes book dictionary as input and dumping it as a string so it will be in json format
# # with open('myfile1213.txt','w') as f:
# #     f.write(s)
#
# with open('myfile1213.txt', 'r') as f:
#     s = f.read()
#     # print(s)
#     book1 = json.loads(s)
#     # print(book1['dip']['name'])
#     for person in book1:
#         print(book1[person])

#
# f = open('/Users/admin/Documents/TestingPython/dip.txt', 'w')
# f.write('Testing Working Successfully')
# f.close()

# with open('/Users/admin/Documents/TestingPython/dip.txt', 'r') as f :
#     # f.write("i love python")
#     s = f.read()
#     print(s)

# problem create a new file which will contain the texts of dip.txt and the word count in beside each line of that line
# f = open('/Users/admin/Documents/TestingPython/dip.txt', 'r')
# f1 = open('/Users/admin/Documents/TestingPython/dip1.txt', 'w')
#
# for line in f:
#     words = line.split(' ')
#     f1.write(' WordCount : '+str(len(words))+' '+line)
#
# f.close()
# f1.close()


# tutorial - if __name__ == "__main__"

# def cal_area(r):
#     print(__name__)
#     return r*r

#
# print(__name__)
#
# n,q = map(int,input().split())
# ara = [0] * (n+1)
# ara = list(map(int,input().split()))
#
# pref = [0] * (n+1)
# for i in range(1,n+1):
#     pref[i] = ara[i-1] + pref[i-1]
#
#
# for i in range(q):
#     l,r = map(int,input().split())
#     print(pref[r]-pref[l-1])

# n = int(input())
# ara = list( map(int,input().split()) )
# pref = [0] * (n+1)
#
# for i in range(n):
#     pref[i] = ara[i] + pref[i-1]
#
#
# q = int(input())
# for i in range(q):
#     l,r = map(int,input().split())
#     if l == 0:
#         print(pref[r])
#     else:
#         print(pref[r] - pref[l-1])
