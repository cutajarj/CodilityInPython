# This is the solution for Leader > Dominator
#
# This is marked as PAINLESS difficulty

def solution(A):
    consecutive_size = 0
    candidate = 0
    for item in A:
        if consecutive_size == 0:
            candidate = item
            consecutive_size += 1
        elif candidate == item:
            consecutive_size += 1
        else:
            consecutive_size -= 1
    occurrence = A.count(candidate)
    if occurrence > (len(A)/2):
        return A.index(candidate)
    else:
        return -1


print(solution([3,0,1,1,4,1,1]))
