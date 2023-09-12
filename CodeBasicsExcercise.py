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

#
# population = {"China":143,"India":136,"USA":32,"Pakistan":21}
# f = 1
# while f :
#     s = input()
#     if s == "print":
#         for i in population:
#             print(i+"==>"+str(population[i]))
#     elif s == "add":
#         name = input()
#         pop = int(input())
#         population[name] = pop
#         print(name + "==>" + str(population[name]))
#     elif s == "remove":
#         name = input()
#         population.pop(name)
#         for i in population:
#             print(i + "==>" + str(population[i]))
#     elif s == "query":
#         name = input()
#         print(population[name])
#         f = 0
#
# import statistics
# stocks = {
#     'info': [600, 630, 620],
#     'ril': [1430, 1490, 1567],
#     'mtl': [234, 180, 160]
# }
#
# def print_all():
#     for stock,price_list in stocks.items():
#         avg = statistics.mean(price_list)
#         print(f"{stock} ==> {price_list} ==> avg: ", round(avg, 2))
#
# def add():
#     s = input("Enter a stock ticker to add:")
#     p = input("Enter price of this stock:")
#     p=float(p)
#     if s in stocks:
#         stocks[s].append(p)
#     else:
#         stocks[s] = [p]
#     print_all()
#
# def main():
#     op=input("Enter operation (print, add or amend):")
#     if op.lower() == 'print':
#         print_all()
#     elif op.lower() == 'add':
#         add()
#     else:
#         print("Unsupported operation:",op)
#
# if __name__ == '__main__':
#     main()

# excecise on files
#
# word = []
# with open('myfile1213.txt','r') as f:
#     for line in f:
#         words = line.split(' ')
#         for i in words:
#             word.append(i)
#
#
# occur = {}
# for w in word:
#     a = word.count(w)
#     occur[w] = a
#
# mx = -1
# for i in occur:
#     if(occur[i]>mx):
#         mx = occur[i]
#
# for i in occur:
#     if mx == occur[i]:
#         print(i)


with open('/Users/admin/Documents/stocks1.csv', 'r') as f:
    with open('/Users/admin/Documents/NEWstocks1.csv', 'w') as f2:
        f2.write("Name,PE ratio,PB ration\n")

        next(f)

        for line in f:
            words = line.split(',')  # made list of every word in the line
            stock = words[0]  # separated them by index
            price = float(words[1])
            eps = float(words[2])
            book = float(words[3])
            pe = round(price / eps, 2)
            pb = round(price / book, 2)
            f2.write(f"{stock},{pe},{pb}\n")
