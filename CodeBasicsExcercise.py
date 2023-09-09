# 1 decimal to binary
num = 5
# print(f"{num} in binary ",format(num,'b'))#inbuilt function
bin = 0
ct = 0
while num != 0:
    bin += int(num % 2) * pow(10, ct)
    num = num / 2
    ct += 1

print(bin)
