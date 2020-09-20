p =[3,1,2,4,3]
right =[]
left = p
sumLeft = 0

for value in p:
    right.append(value)
    del left[p[value]]
    for l in left:
        sumLeft = sumLeft + left
        print('sum Left ' + sumLeft) 

    for r in right:
        abs(sum = sum + right )