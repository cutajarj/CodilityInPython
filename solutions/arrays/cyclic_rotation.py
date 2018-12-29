# This is the solution for Arrays > CyclicRotation
#
# This is marked as PAINLESS difficulty

def solution(A, K):
    result = [None] * len(A)

    for i in range(len(A)):
        result[(i + K) % len(A)] = A[i]

    return result

print(solution([1, 2, 3, 4, 5], 2))

print(solution([1, 2, 3, 4, 5], 5))
