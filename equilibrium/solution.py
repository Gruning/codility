def solution(A):
    sum_left= A[0]
    sum_right= sum(A) - A[0]
    dif = abs(sum_left - sum_right)

    for i in range(1,len(A)-1):
        pass