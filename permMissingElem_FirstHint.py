input = [2, 3, 1, 5]
n = len(input)
result = 0

for x in range(1, n + 1):
    found = False
    for i in input:
        print(f'{x} -- {i}')
        if x == i:
            found = True
            result = i
print(result)


