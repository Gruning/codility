n=5
a=[3,4,4,6,1,4,4]

def solution(n,a):
    maxCounter = 0
    print(a)
    array = [0]* n
   # for cont in array:
    #    cont = 0

    print(array)

    for item in a:        
        print (item)
        if item > n:
            for x in range(0,n-1):
                array[x] = maxCounter 
        else:
            array[item] = array[item] + 1
            if(array[item]>maxCounter):
                maxCounter = array[item]
    
    print(array)

solution(n,a)