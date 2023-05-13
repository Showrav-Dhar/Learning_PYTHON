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

num = 5;


ct = 3
while ct>0:
    a = int(input("Enter Number"))
    if(a==num):
        print("YOU WON THE GAME")
        break
    else:
        print("TRY AGAIN")
        ct-=1





