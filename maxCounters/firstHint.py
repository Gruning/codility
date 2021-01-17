n=5
a=[3,4,4,6,1,4,4]

currentMax=0

def solution(n,a):
    startLine= 0
    maxCounter = 0
    print(a)
    array = [0]* n

    print(array)

    for item in a:        
        print (item)
                
        if(item >= n):
            print('maxCounter in step...')
            print(item)
            startLine = item
        else:
            if(array[item]<startLine):
                array[item]=item + 1
    
        array[item] = array[item] + 1
    print(array)

solution(n,a)
