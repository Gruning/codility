a=[1,2,3,4,5]
k=2
def solution(a,k):
    origLenth = len(a)
    leftOver = k % origLenth

    if leftOver != 0:
        newArrayLen = origLenth + leftOver
    newArray = [0]* newArrayLen
    
    return newArrayLen
