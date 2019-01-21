# This is the solution for Maximum Slice Problem > Max Profit
#
# This is marked as PAINLESS difficulty

def solution(A):
    global_max_sum = 0
    local_max_sum = 0
    for i in range(1, len(A)):
        d = A[i] - A[i - 1]
        local_max_sum = max(d, local_max_sum + d)
        global_max_sum = max(local_max_sum, global_max_sum)
    return global_max_sum


#                      -2160,   112,   243,  -353,   354
print(solution([23171, 21011, 21123, 21366, 21013, 21367]))

