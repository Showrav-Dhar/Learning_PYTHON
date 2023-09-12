# arithmatic operation
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

# Assginment operator
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

# math functions
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

# while loop with else
#
# i = 0
# while(i<4):
#     print(i)
#     i = i + 1
# else:
#     print("IN ELSE BLOCK = ",i)

# while loop with break statement

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


# CAR GAME
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

# Print() function in python

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

# When we slice lists, the start index is inclusive but the end index is exclusive.

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

# remove method
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

# clear      DELETES THE whole list
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

# making a 1d list and taking user input
# n = 5
# ara = [0]*n
# print(len(ara))
# print("Enter 5 numbers in the list")
#
# for i in range(5):
#     a = int(input())
#     ara[i] = a
#
#
# print(ara)
# 2d  LIST

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

rows, cols = (5, 5)
arr = [[0 for i in range(cols)] for j in range(rows)]


#
# arr[0][0] = 1
# arr[2][3] = 10

# for i in range(len(arr)):
#     for j in range(len(arr[i])):
#         print(arr[i][j],end=' ')
#
#     print()


# REMOVE DUPLICATES FROM A LIST
# showrav's solution
#
# l1 = [1,4,1,3,2,3,3,1,2,3,4,5,5]
#
# ct = [0]*(len(l1)+10)
#
# for i in range(len(l1)):
#     ct[l1[i]] += 1
#
# l1.clear()
# for i in range(len(ct)):
#     if(ct[i]!=0):
#         l1.append(i)
#
#
# print(l1)

# mosh solution
#
# nums = [2,2,4,6,3,4,6,1]
# uniqs = []
#
# for i in nums:
#     if i not in uniqs:
#         uniqs.append(i)
#
#
# print(uniqs)

# mosh's solution is better :) in sense of using pythons built in methods

# function to check leap year

# def is_leap(year):
#     leap = False
#
#     if year % 4 == 0 and year%100 !=0:
#         leap = True
#     elif year % 400 == 0:
#         leap = True
#
#     return leap
#
#
# print(is_leap(2100))


# TUPLES

# tuples are immutable

#
# nums = (1,2,3,4,5,2,2,2)
# # print(nums.count(2))
# # print(nums.index((4)))
#
# for i in range(len(nums)):
#     print(nums[i],end=' ')

# unpacking

#
# coordinate = (1,2,3)
# #usual stuff
# # x = coordinate[0]
# # y = coordinate[1]
# # z = coordinate[2]
#
# #python cool stuff
# x, y, z = coordinate # main tuple e joto gulo data thakbe , unpack korar shomoi toto gula variable nite hobe
# #else it will show error, this unpacking method works with list too
# print(x)
# print(y)
# print(z)
#
# l1 = [1,2,3]
# a ,b ,c = l1
# print(a)
# print(b)
# print(c)


#   DICTIONARY
# p1 = {"Name = ": "showrav Dhar","Age ": 20,"Address ":"Jamal Khan"}
# print(p1)

# p1 = {1:10,2:20,3:30,4:40}

# print(p1[3])#p1[key]
# p1[5] = 50 #adding to dictionary
# print(p1)
#
# del p1[2]# key with 2 will be deleted
# print(p1)

# p2 = {3:10,4:20,5:30,9:40}
#
# print(p2.get(4))
# #
# # for i in p2:
# #     print(p2[i])
#
# #digit to word
#
# d_nums = {"0" :"Zero ","1": "One ", "2": "Two ", "3": "Three ", "4": "Four ", "5": "Five ", "6": "Six ", "7": "Seven ", "8": "Eight ","9": "Nine "}
#
# s = input("Enter Your Phone Number ")
#
# for i in s:
#     print(d_nums.get(i),end='')
#   EMOJI CONVERTER
# message = input(">")
# words = message.split(' ')
#
# emojis = {
#     ":)" : "😃",
#     ":(" : "😞",
#     ":')": "🥲",
# }
#
# output = ""
# for i in words:
#     output += emojis.get(i,i) + " "
#
#
# print(output)
#

# functions

# def fun():
#     print("HELLO DIP")
#
# for i in range(10):
#     fun()

# def add (a,b):
#     return  a+b
#
# print(add(10,20))


# def greet(fname,lname):
#
#     print(f"{fname} {lname} Welcome")
#
# greet("Showrav","Dhar")


# def greet(fname,lname):
#     print(f"Hello {fname} {lname}")
#
#
# print(greet(lname="dhar",fname="Showrav"))#key word arguments
# #function e argument er jei name disi , function call korar time e amra defeine kore
# #dichhi argument er nam gula


# reusable function
# def emoji_converted(user_message):
#     given_message = user_message
#     words = given_message.split(' ')
#
#     emojis = {":)": "😃", ":(": "😞", ":')": "🥲"}
#     converted = ""
#     for word in words:
#         converted += emojis.get(word, word) + " "
#
#     return converted
#
#
# message = ""
#
# while message != "bye":
#     message = input("Type A Message > ")
#     print(emoji_converted(message))


# Python built in exception
# print(dir(locals()['__builtins__']))
#
# try:
#     age = int(input("Enter Age > "))
#     income = 20000
#     risk = income/age
#     print(age)
#     print(risk)
# except ZeroDivisionError :
#     print("Age cannot be zero")
# except ValueError:
#     print("INVALID VALUE")

# PYTHON OOP

# class room:
#
#     length = 0.0
#     bredth = 0.0
#
#     def calculate_area(self):
#         print("Area of the room = ",self.length *self.bredth)
#
#
# bedroom = room()
# bedroom.length = 10
# bedroom.bredth = 20
# bedroom.calculate_area()
#
# study_room = room()
# study_room.bredth = 30
# study_room.length = 40
# study_room.calculate_area()

# class Bike:
# #CONSTRUCTOR
#     def __init__(self,name = ""):
#         self.name = name
#
#
#
# b1 = Bike("Mountain Bike")
# print(b1.name)


# class Person:
#     def __init__(self,name = "",age = 0):#constructor of the class
#         self.name = name
#         self.age = age
#
#     def talk(self):# method of a class
#         print(f"{self.name} is talking")
#
#
#
# p1 = Person("Showrav Dhar",23)
# print(p1.name)
# print(p1.age)
# p1.talk()
#
# p2 = Person("Showmik Dhar",24)
# print(p2.name)
# print(p2.age)
# p2.talk()
#
# INHERITANCE

# class animal:
#     animal_name = ""
#
#     def eat(self):
#         print(f"{self.animal_name} is eating now")
#
#     def sleep(self):
#         print(f"{self.animal_name} is sleeping now")
#
#
# class dog(animal):
#     def __init__(self,name):
#         self.animal_name = name
#
#     def sounds_Like(self):
#         print(f"{self.animal_name} sound bark bark !!!!")
#
#
#     def eat(self): #method over_riding
#         print(f"{self.animal_name} Loves to eat Bones")
#
#     #super method
#
#     def sleep(self):
#         super.sleep()
#         print()
#
#
#
# d1 = dog("Tommy")
# print(d1.animal_name)
# d1.eat()
# d1.sleep()
# d1.sounds_Like()


# working with modules
#
# import dip_module
#
# print(dip_module.add_dip(10,20))
# print(dip_module.subtract_dip(5,10))

# importing module with renaming
# import dip_module as dm
# print(dm.subtract_dip(10,20))
# print(dm.add_dip(30,20))

# working with packages

#
# import Ecommerce.shipping
#
# Ecommerce.shipping.calculate_shipping()

# from Ecommerce.shipping import calculate_shipping, calculate_total_prods

# to import the entire module
# #
# from Ecommerce import shipping # called the shipping module from the package Ecommerce
# #from package import module
# shipping.calculate_shipping()
# shipping.calculate_total_prods()


# generating random values
# import random

# for i in range(5):
#     # print(random.random())
#     print(random.randint(10, 20))#Random values within the range of 10 - 20

#
# l1 = ["antu","dip","Richi","Lamisa"]
# person = random.choice(l1)#Randomly selects an item from the list
# print(person)
#
# dice game
#
# import random
#
#
# class dice:
#     def roll(self):
#         first_num = random.randint(1, 6)
#         second_num = random.randint(1, 6)
#         return first_num, second_num
#
#
# d1 = dice()
# print(d1.roll())

# working with directories


# absolute path [ /usr/local/bin ]
# relative path

#
# from pathlib import Path
#
# # path = Path("Ecommerce")  # created an object of path class
# # print(path.exists())
#
# path = Path("Customers")  # created a new directory using class fucntion
# print(path.mkdir())

# to remove directory
# print(path.rmdir()) #Customers directory removed

# to find all the py files in a directory
#
# from pathlib import Path
#
# path = Path()
# # print(path.glob("*.py"))
# #iterating through the files
# # for file in path.glob("*py"): #glob method is use to find a type of file all over the diretory
# #     print(file)
# #to show all the files in the directory
#
# for file in path.glob("*"):# all the files in the directory
#     print(file)

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

# Reading a file
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

# working with json file in python
# infoBook = {}
#
# infoBook['dip'] = {
#     'name' : 'dip',
#     'age'  : '23',
#     'gender': 'male'
# },
# infoBook['antu']= {
#     'name' : 'antu',
#     'age'  : '28',
#     'gender': 'male'
# }
# import json
# # s = json.dumps(infoBook)
# # with open('myfile1213.txt','w') as f:
# #     f.write(s)
#
# with open('myfile1213.txt','r') as f :
#     s = f.read()
#     infoBook1 = json.loads(s)
#
#     for person in infoBook1:
#         print(infoBook1[person])
#
# line = "Hello i am showrav"
# words = line.split(' ')
#
# import CodeBasics
# print(CodeBasics.cal_area(10))
#

# Exception Handling

# a = "20"
# b = 10
#
# try:
#
#     print(a/b)
# except Exception as e:
#     print("Type of Exception = ",e)
#
#
# print("Hello dip ")


# classes and object

# class person:
#     name = "Showrav"
#     Occupation = "Software Engineer"
#     networth = "1000k"
#     def info(self):
#         print(f"{self.name} is a {self.Occupation}")
#
# a = person()
# a.info()

# Constructor
# class Person:
#     def __init__(self,name,occ):
#         self.name = name
#         self.occ = occ
#
#
#     def info(self):
#         print(f"{self.name} is a {self.occ}")
#
#
# p1 = Person("Showrav Dhar","SDE")
# p1.info()


# inheritance
#
# class MobileApp:  # base class
#     def general_use(self):
#         print("Used in Mobile Phone")
#
#
# class FoodDeliveryApp(MobileApp):
#     def __init__(self):
#         print("It is a food delivery app")
#
#     def specific_use(self):
#         self.general_use()
#         print("It can be used to order food")
#
#
# class RideSharing(MobileApp):
#     def __init__(self):
#         print("It is a Ride Sharing app")
#
#     def specific_use(self):
#         self.general_use()
#         print("It can be used to share Ride")
#
#
# a1 = FoodDeliveryApp()
# print(isinstance(a1,FoodDeliveryApp))
# print(isinstance(a1,RideSharing))
# print(issubclass(RideSharing,MobileApp))
#


# #multiple inheritance
# class dad:
#     def D_skills(self):
#         print("Retierd SDE")
#
# class mom:
#     def M_skills(self):
#         print("Ex-Product Manager of Bkash")
#
#
# class son(dad,mom):
#     def designer(self):
#         print("UI/UX designer At Google")
#
#     def skills(self):
#         dad.D_skills(self)
#         mom.M_skills(self)
#
#
# p1 = son()
# p1.D_skills()
# p1.M_skills()
# p1.designer()
# p1.skills()
#
# import statistics
#
# stocks = {
#     'info': [600, 630, 620],
#     'ril': [1430, 1490, 1567],
#     'mtl': [234, 180, 160]
# }
#
# def print_all():
#     for i in stocks:
#         a = statistics.mean(stocks[i])
#         print(f"{i}==>{stocks[i]}==> avg = ",round(a,2))
#
# def add():
#     name = input("Enter stock name  ->")
#     price = int(input("Enter Stock price    ->"))
#
#     if name in stocks:
#         stocks[name].append(price)
#     else:
#         stocks[name] = [price]
#     print_all()
#
# if __name__ == '__main__':
#     print_all()
#     add()
l = ['dip','dip','antu']
print(l.count('dip'))