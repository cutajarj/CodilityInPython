# This is the solution for Caterpillar Method > CountDistinctSlices
#
# This is marked as PAINLESS difficulty

def solution(M, A):
    total_slices = 0
    in_current_slice = [False] * (M + 1)
    head = 0
    for tail in range(0,len(A)):
        while head < len(A) and (not in_current_slice[A[head]]):
            in_current_slice[A[head]] = True
            head += 1
            total_slices += (head - tail)
            total_slices = 1000000000 if total_slices > 1000000000 else total_slices
        in_current_slice[A[tail]] = False
    return total_slices


print(solution(6, [3, 4, 5, 5, 2]))

print(solution(6, [3, 5, 4, 5, 2]))

print(solution(6, [5, 3, 4, 2, 5]))

print(solution(6, [5, 5, 5, 4, 5]))

print(solution(6, [5]))

print(solution(1, [0,1]))

