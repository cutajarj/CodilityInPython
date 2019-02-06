# This is the solution for Prefix Sums > Count Div
#
# This is marked as RESPECTABLE difficulty

from math import ceil, floor


def solution(A, B, K):
    n_start = ceil(A / K)
    n_end = floor(B / K)
    return n_end - n_start + 1


print(solution(6, 11, 2))
