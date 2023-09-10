# # 1 decimal to binary
# num = 5
# # print(f"{num} in binary ",format(num,'b'))#inbuilt function
# bin = 0
# ct = 0
# while num != 0:
#     bin += int(num % 2) * pow(10, ct)
#     num = num / 2
#     ct += 1
#
# print(bin)
# n = 5
# r = 2
# sum = 1
#
# # Calculate the value of n choose r using the binomial coefficient formula
# for i in range(1, r+1):
# 	sum = sum * (n - r + i) / i
#
# print(int(sum))
# # This code is contributed by divyansh2212

#
# s='Earth revolves around the sun'
# print(s[6:13])
# print(s[-3:])
#
# fruit = 10
# veg = 3;
# print(f"I eat {veg} veggies and {fruit} fruits daily.")
#
# s = "i ate 10 burgers today"
# s = s.replace('10','5')
# s = s.replace('burgers','chicken fries')
# print(s)
#
# s = "i ate 20 Mangoes today"
# s = s.replace('20','30').replace('Mangoes','apples')
# print(s)
# result = ["heads","tails","tails","heads","tails","heads","heads","tails","tails","tails"]
# ct = 0
# for i in result:
#     if i == "heads":
#         ct+=1
#
# print(ct)


population = {"China":143,"India":136,"USA":32,"Pakistan":21}
f = 1
while f :
    s = input()
    if s == "print":
        for i in population:
            print(i+"==>"+str(population[i]))
    elif s == "add":
        name = input()
        pop = int(input())
        population[name] = pop
        print(name + "==>" + str(population[name]))
    elif s == "remove":
        name = input()
        population.pop(name)
        for i in population:
            print(i + "==>" + str(population[i]))
    elif s == "query":
        name = input()
        print(population[name])
        f = 0

