# This is the solution for Greedy algorithms > MaxNonoverlappingSegments
# The problem is equivalent to the Activity Selection Problem,
# where you have to choose the maximum non overlapping tasks.
#
# This is marked as PAINLESS difficulty

def solution(A, B):
    last_end_segment = -1
    chosen_count = 0
    for i in range(len(A)):
        if A[i] > last_end_segment:
            chosen_count += 1
            last_end_segment = B[i]
    return chosen_count



print(solution([1, 3, 7, 9, 1], [5, 6, 8, 9, 10]))

print(solution([1, 3, 5, 7, 9], [2, 4, 6, 8, 10]))

print(solution([], []))
