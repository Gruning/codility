p =[3,1,2,4,3]
right = p
left = []
sumLeft = 0
sumRight = 0
cont = 0

print('p',p)
for value in p:
    print('value', value)
    left.append(value)
    print('cont', cont)
    print('array', value)
    print('left',left)
    del right[cont]
    cont = cont + 1
    print('right',right)
    # print('right',right)

    # for l in left:
    #     sumLeft = sumLeft + l
    #     print('sum Left ',sumLeft) 

    # for r in right:
    #     if right != []:
    #         print('sum right ',sumRight) 
        #abs(sum = sum + right )