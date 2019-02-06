# This is the solution for Prefix Sums > Count Div
#
# This is marked as RESPECTABLE difficulty

from math import ceil, floor


def solution(A, B, K):
    n_start = ceil(A / float(K))
    n_end = floor(B / float(K))
    return n_end - n_start + 1


print(solution(6, 11, 2))
