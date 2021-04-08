# This is the solution for Caterpillar Method > MinAbsSumOfTwo
#
# This is marked as RESPECTABLE difficulty


def solution(A):
    min_abs_sum = 2000000000
    A = sorted(A)
    head = 0
    tail = len(A) - 1
    while head <= tail:
        min_abs_sum = min(min_abs_sum, abs(A[head] + A[tail]))
        if A[head] + A[tail] < 0:
            head += 1
        else:
            tail -= 1
    return min_abs_sum


print(solution([-7, 3, -1, 5, -11, 4, -9, 14, 17, -2]))  # Solution should be 1
print(solution([8, 3, 5, 16, 11]))  # Solution should be 6
print(solution([-7, -5, -6, -2, -9]))  # Solution should be 4
print(solution([-7, 3, -6, 1, 0, -9]))  # Solution should be 0
print(solution([-22, 3, 4, 5]))  # Solution should be 6
