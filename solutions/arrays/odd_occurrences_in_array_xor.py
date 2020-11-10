# This is the alternative (consumes less memory) solution for Arrays > OddOccurrencesInArray
#
# This is marked as PAINLESS difficulty


def solution(A):
    result = 0
    for i in range(0, len(A)):
        result ^= A[i]
    return result


print(solution([1, 4, 4, 1, 6, 8, 6]))

