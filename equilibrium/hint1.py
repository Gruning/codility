p =[3,1,2,4,3]
right = p
left = []
sumLeft = 0
sumRight = 0
# _cont = 0

print('p',p)
for valueL in p:
    print('valueL', valueL)
    left.append(valueL)
    # print('cont', _cont)
    # print('array', value)
    print('left',left)

print('--------')
for valueR in p:
    print('valueR', valueR)
    right.remove(valueR)
    #del right[_cont]
    # _cont = _cont + 1

    print('right',right)

    # for l in left:
    #     sumLeft = sumLeft + l
    #     print('sum Left ',sumLeft) 

    # for r in right:
    #     if right != []:
    #         print('sum right ',sumRight) 
        #abs(sum = sum + right )