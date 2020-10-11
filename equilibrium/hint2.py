p =[3,1,2,4,3]
_sum = sum(p)
right=[]
left = []
sumLeft = _sum
sumRight = _sum
for r in range (1,len(p)):
    print('r ',r )
    print('p[r] ', p[r])
    sumRight = sumRight - p[r-1]
    print('sumrigth ', sumRight)


print(_sum)
