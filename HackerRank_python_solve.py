#   BASIC DATA TYPES SECTION ON HackerRANK

# Find the Runner-Up Score!

# if __name__ == '__main__':
#     n = int(input())
#     arr = list(map(int, input().split()))
#
#
#     l1 = list(set(arr))
#     len1 = len(l1)
#     l1.sort()
#     print(l1[len1-2])

# LISTS
#
# N = int(input())
# ans_l = []
# for i in range(N):
#     l1 = input().split(' ')
#
#     if len(l1) == 1:
#         if l1[0] == "sort":
#             ans_l.sort()
#         elif l1[0] == "pop":
#             ans_l.pop(-1)
#         elif l1[0] == "reverse":
#             ans_l.reverse()
#         elif l1[0] == "print":
#             print(ans_l)
#     elif len(l1) == 2:
#         if l1[0] == "append":
#             ans_l.append(int(l1[1]))
#         elif l1[0] == "remove":
#             ans_l.remove(int(l1[1]))
#     elif len(l1) == 3:
#         if l1[0] == "insert":
#             ans_l.insert(int(l1[1]), int(l1[2]))
#
# TUPLES
# if name == 'main':
#     n = int(input())
#     integer_list = map(int, input().split())
#     print
#     (hash(tuple(integer_list)))


# def swap_case(s):
#     str = ''
#     for i in s:
#         if i.islower():
#             str += i.upper()
#         # print(i.upper(),end='')
#         elif i.isupper():
#             str += i.lower()
#         # print(i.lower(),end='')
#         else:
#             str += i
#         # print(i,end='')
#     return str
#
# s = input()
# ans = swap_case(s)
# print(ans)



# occurence of a substring in a string using python
# def count_substring(string, sub_string):
#     count = 0
#     start = 0
#
#     while start<len(string):
#
#         pos = string.find(sub_string,start)
#
#         if pos!=-1:
#             start = pos+1
#             count+=1
#         else:
#             break
#
#
#     return count
#
# print(count_substring("ABCDCDC","CDC"))

if __name__ == '__main__':
    t = int(input())
    for tc in range(t):
        n,k,x = map(int,input().split())

        sum1 = (k*(k+1))/2

        sum2 = (k*(2*n-k+1))/2

        if x<sum1 or x>sum2:
            print("NO")
        else:
            print("YES")








