p =[3,1,2,4,3]
right=[]
for r in p:
    right.append(r)

left = []
sumLeft = 0
sumRight = 0

print('p',p)
for valueL in p:
    print('valueL', valueL)
    left.append(valueL)
    print('left',left)

print('--------')
cont = 0 
for valueR in p:
    print('valueR', valueR)
    right.remove(valueR)
    cont = cont + 1

    print('right',right)

