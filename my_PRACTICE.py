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


game_run = True
stp = 0
strt = 0
while(game_run) :
    a = input("> ")

    if(a.lower() == "help"):
        print("Start = Starting The Car\n")
        print("Stop = Stopping The Car\n")
        print("Quit = Qutting The Game\n")

    elif (a.lower()=="start" and strt == 0):
        print("Starting the car")
        strt+=1
    elif (a.lower() == "start" and strt >= 1):
        print("THE CAR IS ALREADY STARTED")
        strt += 1
    elif (a.lower()=="stop" and stp==0):
        print("Car is already stopped")
        stp+=1
    elif (a.lower() == "stop" and stp >= 1):
        if(stp==1):
            print("THE CAR IS  STOPPED")
        else:
            print("THE CAR IS ALREADY STOPPED")
        stp+= 1
    elif(a.lower() == "quit"):
        game_run = False
    else:
        print("I don't understand that")
