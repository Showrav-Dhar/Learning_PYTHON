# is_hot = False
# is_cold = False
#
#
# if is_hot:
#     print("Its a hot day")
#     print("Drink enough water")
# elif is_cold :
#     print("It is a cold day")
#     print("wear warm clothes")
# else :
#     print("Its a lovely day")
# print("Enjoy Your Day")
#
#
# good_credit = True
#
# if good_credit:
#     c = 0.1 * 1000000
#     print(f"Down Payment = ${c}")
# else :
#     c = 0.2 * 1000000
#     print(f"Down Payment =  ${c}")

# a = input("Enter Your Name = ")
#
# if (len(a)<3) :
#     print("Your Name Must be at least 3 characters long")
# elif (len(a)>50):
#     print("Your Name Can Be Maximum 50 Characters Long")
# else:
#     print("Name Looks Good")

#Weight Converter
# import math
#
# w = int(input("Enter Your Weight = "))
# c = input("(L)bs or (k)g = ")
# if (c=='l' or c=='L'):
#     kg = math.ceil(w * 0.453592)
#     print("Your Weight In kilos = ",kg)
# elif (c=='K' or c=='k'):
#     pd = math.ceil(w * 2.20462)
#     print("Your Weight In Pound = ",pd)

#
# i = 1
# while(i<5):
#     print(i* '*')
#     i+=1

#cargame

#
# game_run = True
# stp = 0
# strt = 0
# while(game_run) :
#     a = input("> ")
#
#     if(a.lower() == "help"):
#         print("Start = Starting The Car\n")
#         print("Stop = Stopping The Car\n")
#         print("Quit = Qutting The Game\n")
#
#     elif (a.lower()=="start" and strt == 0):
#         print("Starting the car")
#         strt+=1
#     elif (a.lower() == "start" and strt >= 1):
#         print("THE CAR IS ALREADY STARTED")
#         strt += 1
#     elif (a.lower()=="stop" and stp==0):
#         print("Car is already stopped")
#         stp+=1
#     elif (a.lower() == "stop" and stp >= 1):
#         if(stp==1):
#             print("THE CAR IS  STOPPED")
#         else:
#             print("THE CAR IS ALREADY STOPPED")
#         stp+= 1
#     elif(a.lower() == "quit"):
#         game_run = False
#     else:
#         print("I don't understand that")

# for loop

# to print range of number in one line
# for item in range(10):
#     print(item , end = ' ')
#
# for item in ['dip', 'antu', 'richi']:
#     print(item, end=' ')


# increment value
#
# for item in range(1,10,2):
#     print(item,end=' ')
# #   1 3 5 7 9

#
# prices = [10, 20, 30, 40, 50]
# total = 0
# for it in prices:
#
#     total+=it
#
# print(f"Total Price Is {total}\n")


#   user input in loop
#
# price = 0
# total = 0
# for t in range(5):# loop will run for 5 times
#     print(f"Enter Price of Product = {t+1}")
#     price = int(input())
#     total += price
#
#
# print(f"Total Price Is {total}\n")


#nested loops

# for i in range(1,7):
#     for j in range(1,i):
#             print('*',end =' ')
#
#     print('\n')

#
# for x in range(5):
#     for y in range(5):
#         print(f'({x}, {y})',end = ' ')
#
#     print('\n')

#
# for x in range(5):
#     if(x==0 or x==2):
#         for y in range(5):
#             print("x", end='')
#     else:
#         for y in range (2):
#             print("x", end='')
#     print()


# PRACTICE MAKING PATTERNS WITH NESTED LOOP TO CLEAR ALL PROBLEMS ON
# NESTED LOOPS
#
# for i in range (6):
#     for j in range (i):
#         print("*",end='')
#     print()
# *
# **
# ***
# ****
# *****
#
# for i in reversed(range (6)):
#     for j in range(6):
#         if(j>=i):
#             print("*",end='')
#         else:
#             print(" ",end='')
#     print()
#      *
#     **
#    ***
#   ****
#  *****
# ******
#
# for i in reversed(range(6)):
#     for j in reversed(range(i)):
#         print("*",end='')
#     print()
#
#
# *****
# ****
# ***
# **
# *

# for i in reversed(range(6)):
#     for j in reversed(range(6)):
#         if(j<=i):
#             print("*",end='')
#         else:
#             print(" ",end='')
#     print()

#
# ******
#  *****
#   ****
#    ***
#     **
#      *

# for i in reversed(range(6)):
#     for j in range(6):
#         if(j>=i):
#             print("* ",end='')
#         else:
#             print(" ",end='')
#
#     print()

#      *
#     * *
#    * * *
#   * * * *
#  * * * * *
# * * * * * *










