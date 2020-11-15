a=[1,2,3,4,5]
k=7
#def solution(a,k):
#origLenth = len(a)
print(len(a))
leftover =  k % len(a)
print(leftover)
print('-------')
#newArray = a 

if leftover != 0:
    #newArrayLen = origLenth + leftOver
    for elem in range(leftover , len(a)):
        print(a[elem])        
    for elem in range(leftover):
        print(a[elem])
#return newArray