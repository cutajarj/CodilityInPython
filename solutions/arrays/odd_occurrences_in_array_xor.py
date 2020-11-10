# This is the alternative (consumes less memory) solution for Arrays > OddOccurrencesInArray
#
# This is marked as PAINLESS difficulty


def solution(A):
    result = A[0]
    for i in range(1, len(A)):
        result ^= A[i]
    return result


print(solution([9, 3, 9, 3, 9, 7, 9]))

