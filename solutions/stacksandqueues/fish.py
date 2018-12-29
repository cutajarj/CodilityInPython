# This is the solution for Stacks And Queues > Fish
#
# This is marked as PAINLESS difficulty

def solution(A, B):
    stack = []
    survivors = 0
    for i in range(len(A)):
        weight = A[i]
        if B[i] == 1:
            stack.append(weight)
        else:
            weightdown = stack.pop() if stack else -1
            while weightdown != -1 and weightdown < weight:
                weightdown = stack.pop() if stack else -1
            if weightdown == -1:
                survivors += 1
            else:
                stack.append(weightdown)
    return survivors + len(stack)

print(solution([4, 8, 2, 6, 7], [0, 1, 1, 0, 0]))

print(solution([4, 3, 2, 1, 5], [0, 1, 0, 0, 0]))