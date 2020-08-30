input = [2, 3, 1, 5]
secondArray = [None] * (len(input) + 2)
print(len(secondArray))

for x in input:
    secondArray[input[x]] = False

print(secondArray)

notlast = len(secondArray) - 1

for y in range(1, notlast):
    print(secondArray[y])
    if secondArray[y]:
        print(y)
