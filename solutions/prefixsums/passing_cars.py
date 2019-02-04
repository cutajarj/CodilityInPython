# This is the solution for Prefix Sums > Passing Cars
#
# This is marked as PAINLESS difficulty

def solution(A):
    suffix_sum = [0] * (len(A) + 1)
    for i in range(len(A) - 1, -1, -1):
        suffix_sum[i] = A[i] + suffix_sum[i + 1]

    count = 0
    for i in range(len(A)):
        if A[i] == 0:
            count += suffix_sum[i]
        if count > 1000000000:
            return -1

    return count


print(solution([0, 1, 0, 1, 1]))
