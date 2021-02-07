def solution(N,A):
    counters = 0*N
    start_line = 0
    current_max = 0

    for i in A:
        x = i-1
        if i > N:
            start_line = current_max
        