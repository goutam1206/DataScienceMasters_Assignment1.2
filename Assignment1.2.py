numList = list()
for num in range(2000, 3200):
    if (num%7 == 0 and num % 5 != 0):
        numList.append(num)
print (numList)