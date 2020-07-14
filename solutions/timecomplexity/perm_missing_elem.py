# This is the solution for Time Complexity > PermMissingElem
#
# This is marked as PAINLESS difficulty


def solution(A):
    actual_sum = 0
    for number in A:
        actual_sum += number
    max_number = len(A) + 1
    expected_sum = (max_number * (max_number + 1) // 2)
    return expected_sum - actual_sum


print(solution([2, 3, 1, 5]))

print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9]))

print(solution([]))
