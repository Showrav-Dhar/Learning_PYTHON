#arithmatic operation
# a = 7
# b = 4;
# c = a+b
# print(f"Sum(+) of {a} {b} = ",c)
# print(f"Subtraction(-) of {a} {b} = ",a-b)
# print(f"Multiplication(*) of {a} {b} = ",a*b)
# print(f"Division(/) of {a} {b} = ",b/a)
# print(f"Modulo(%) of {a} {b} = ",a%b)
#
# print(f"Floor division(//) of {a} {b} = ",a//b)
# print(f"power operator( b ** a) -> {b} to the power {a} = ", b**a)

#Assginment operator
# a = 7
# b = 5
# a+=b

# print(a)
# a-=3
# print(a)
# a*=10
# print(a)
# a/=2
# print(a)
# a%=4
# print(a)
# a**=2
# print(a)

#math functions
#
# import  math
# x = 2.9
# print(round(x))
# k = -1
# print(abs(k))
# print(math.ceil(x))
# print(math.floor(x))

# If statement

# 1) if statement
#
# a = 10
#
# if (a%2 == 0) :
#     print("This is a even number")
#
# # 2) if..else statement
#
#     if(a<4):
#         print("testing if block")
#     else :
#         print("testing else block")
#
# # 3) if..elif..else
#
#     c = 100
#
#     if(c<10):
#         print("Testing if block")
#     elif (c>10 and c<=100):
#         print("testing else if block")
#     else:
#         print("Testing else block")

# Nested if statment
# num = 5;
# #Outer if statement
# if(num >= 0):
#     # inner if statement
#     if(num == 0):
#         print("The number is zero")
#     # inner else statement
#     elif (num > 0):
#         print("the number is positive")
#
# #Outer else statement
# else:
#     print("The number is negative")


# while loop
# i = 0;
# while (i<=5):
#     print(i)
#     i = i+1


#
# a = int(input())
# while(a!=0):
#     print(a)
#     a = int(input())


# Infinite While loop
# while(1):
#     print("HELLO")

#while loop with else
#
# i = 0
# while(i<4):
#     print(i)
#     i = i + 1
# else:
#     print("IN ELSE BLOCK = ",i)

#while loop with break statement

# i = 0
# while(i<10):
#     print(i)
#     if(i==4):
#         break
#     i+=1

## GUESSING GAME

# num = 5;
#
#
# ct = 3
# while ct>0:
#     a = int(input("Enter Number"))
#     if(a==num):
#         print("YOU WON THE GAME")
#         break
#     else:
#         print("TRY AGAIN")
#         ct-=1
#


#CAR GAME
#
# gamerun = True
# while(gamerun):
#     a = input("> ")
#     if (a == "Help" or a == 'help'):
#         print("Start - To Start The Car\n"
#               "Stop - To Stop The Car\n"
#               "Quit - To Quit The Car\n")
#     elif(a=="Start" or a=="start"):
#         print("Starting The Car, Ready To Go In 3...2..1.")
#     elif(a=="Stop" or a=="stop"):
#         print("Stopping The Car")
#     elif(a=="Quit" or a=="quit"):
#         gamerun = False
#     else:
#         print("I Don't Understand That....")


# for loop
#
# for i in range(10):
#     print(i)
#
# for ch in 'Showrav':
#     print(ch)

# #
# for i in reversed(range(6)):
#     for j in range(6):
#         if(j>=i):
#             print("* ",end='')
#         else:
#             print(" ",end='')
#     print()
#
#

#Print() function in python

# FORMATTING

# a = "bangladeshis"
# b = "Mangoes"
#
# print("{0} loves {1}".format(a, b))
# c = "Apples"
# d = "Americans"
# print("{0} loves {1}".format(c, d))
#
# x = "Apple Products"
# y = "Engineers"
# print(f"{y} loves using {x}")
#
# a = 10
# b = 20
# print(a, " + ", b, " = ", a+b)
# print(f"{a} + {b} = ", a+b)
#
# c = 30
# d = 50
# print("you entered %d and %d " % (c, d))


# SEPARATOR
# print("HELLO", "DIP", "ANTU", "RICHI", sep=',') # HELLO,DIP,ANTU, RICHI
# print("HELLO", "DIP", "ANTU", "RICHI", sep='\n')
# HELLO
# DIP
# ANTU
# RICHI

# END

# a = 10
# b = 20
# c = 30
# print(a, b, c, end=' ')


# LIST
# numbers = [1,2,5]
# print(numbers)
# #
# my_list = [1,2,"DIP",1.2,1.4]
# # print(my_list)
#
# for i in range(5):
#     print(my_list[i],end=' ')
#
# ara = [10,20,304,50,60]
#
# print(ara[1:3]) # output = [20, 304]
# print(ara[2:]) # output = [304, 50, 60]
# print(ara[2:4]) # output =[304, 50]

#When we slice lists, the start index is inclusive but the end index is exclusive.

# Add Elements to a Python List
# append()
# ara = [10,30,40,50,60]
#
# print(ara)
#
# ara.append(200)
# print(ara)

# # extend()
#
# list1 = [1,2,3,4]
# list2 = [10,20,30,40,50]
# list1.extend(list2)
# print(list1)

# Change List Items
# list1 = [1,2,3,4]
# print(list1)
# list1[2] = 10
# print(list1)
# Remove an Item From a List
#
# del method
# list1 = [1,2,3,4]
# print(list1)
# del list1[2]
# print(list1)

#remove method
# list1 = ["dip","antu","Richi","Showrav"]
# print(list1)
# list1.remove("antu")
# print(list1)
# list1.append("MESSI")
# print(list1)
#
# list1 = [1,2,3,4]
# list1.remove(2)
# print(list1)

#clear      DELETES THE whole list
# list1 = [1,2,3,4]
# print(list1)
# list1.clear()
# print(list1)

# # sort
# list1 = [4,1,3,2]
# print(list1)
# list1.sort()
# print(list1)
#

# check if a item is present in the list
# list1 = ["apple","mango","watermelon","Banana"]
#
# len_of_list = len(list1)
# f = False
# for it in range(len_of_list):
#     if(list1[it] == "mango"):
#         print(f"{list1[it]} is present in the list\n")
#         f = True
#         break
#
# if f==False:
#     print("Mango is not present in the list")


# List Comprehension
# list1 = [1,2,3,4,5]
#
# for it in range(len(list1)):
#     list1[it] = list1[it]*list1[it]
#
#
# print(list1)










