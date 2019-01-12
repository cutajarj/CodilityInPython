# This is the solution for Time Complexity > TapeEquilibrium
#
# This is marked as PAINLESS difficulty

def solution(A):
    sum_left = A[0]
    sum_right = sum(A) - A[0]
    diff = abs(sum_left - sum_right)
    for i in range(1, len(A)-1):
        sum_left += A[i]
        sum_right -= A[i]
        current_diff = abs(sum_left - sum_right)
        if diff > current_diff:
            diff = current_diff
    return diff


print(solution([3, 1, 2, 4, 3]))


