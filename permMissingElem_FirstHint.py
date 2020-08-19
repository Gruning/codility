input = [2, 3, 1, 5]
n = len(input) + 1
result = 0

for x in n:
    found = False
    for i in input:
        if i == x:
            found = True
            result = i
print(result)


