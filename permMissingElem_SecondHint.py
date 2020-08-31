input = [2, 3, 1, 5]
secondArray = [None] * (len(input) + 2)
lenSecond = len(secondArray)
print(len(secondArray))

for x in input:
    secondArray[x] = False

print(secondArray)

notlast = len(secondArray) - 1

for y in range(1, lenSecond):
    #print(secondArray[y])
    if secondArray[y] is None:
        print(f'missing ', y)
