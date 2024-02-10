# problem 1
# str1 = input("Enter a word : ")
# str2 = input("Enter another word : ")
# print("Display Pattern")
# len1 = len(str1)
# len2 = len(str2)
#
# if len1 > len2:
#     for i in range(0, len2):
#         print(f"Index {i}: " + str1[i] + str1[i] + " - " + str2[i] + str2[i])
#
#     for i in range(len2, len1):
#         print(f"Index {i}: " + str1[i] + str1[i] + " - " + "?" + "?")
# else:
#     for i in range(0, len1):
#         print(f"Index {i}: " + str1[i] + str1[i] + " - " + str2[i] + str2[i])
#
#     for i in range(len1, len2):
#         print(f"Index {i}: " + "?" + "?" + " - " + str2[i] + str2[i])

# problem 2
# start = int(input("Enter start integer: "))
# end = int(input("Enter end integer: "))
# c1 = input("Enter a letter: ")
# c2 = input("Enter another letter: ")
# print("Here is the output pattern:")
#
# dif = end - start
# dimension = 2 * dif + 2
# dimension += 1  # to iterate from 1 to dimension
#
# for i in range(1, dimension):
#     num = start
#     for j in range(1, i + 2):
#         if i % 2 == 0:
#             print(c2, end=' ')
#             break
#         elif i % 2 == 1 and j % 2 == 0:
#             print(c1, end=' ')
#         else:
#             print(num, end=' ')
#             num += 1
#     print()

# # problem 3
# num = int(input("Enter an integer: "))
# i = 1
# while num >= 10:
#     if num % 2 == 0:
#         print(f"Step {i}: {num} even, divided by 2 -> {num}/{2} = {num//2}")
#         num = num // 2
#         i += 1
#     elif num % 2 == 1:
#         print(f"Step {i}: {num} odd, minus 5 -> {num}-{5} = {num-5}")
#         num = num - 5
#         i += 1
# print(f"Step {i}: {num} is less then 10 -> stop now")

# BFS
# Python3 Program to print BFS traversal
# from a given source vertex. BFS(int s)
# traverses vertices reachable from s.
