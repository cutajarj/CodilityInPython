# This is the solution for Time Complexity > PermMissingElem
#
# This is marked as PAINLESS difficulty


def solution(A):
    max_number = len(A) + 1
    sum = 0
    for number in A:
        sum += number
    return (max_number * (max_number + 1) // 2) - sum


print(solution([2, 3, 1, 5]))

print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9]))

print(solution([]))
