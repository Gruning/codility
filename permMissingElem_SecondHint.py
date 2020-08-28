input = [2, 3, 1, 5]
secondArray = [None] * (len(input) + 2)
print(len(secondArray))

for x in input:
    secondArray[x] = False

notlast = len(secondArray) - 0

for y in range(1, notlast):
    if secondArray[y]:
        print(y)
