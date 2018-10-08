# This is the solution for Dynamic programming > NumberSolitaire
#
# This is marked as RESPECTABLE difficulty
# Note here we have the evolution of the algorithm. Only the last function is the correct one.

def solutionRecursive(A):
    return max_sum_six_distances(A, 0)


def max_sum_six_distances(a, position):
    if position == len(a) - 1:
        return a[position]
    else:
        max_forward = min(len(a) - position, 6)
        current_max = -100000
        for i in range(1, max_forward):
            local_max = max_sum_six_distances(a, position + i)
            current_max = max(current_max, local_max)
        return current_max + a[position]


def solutionMemoize(A):
    values = [-100000] * len(A)
    return max_sum_six_distancesMem(A, 0, values)


def max_sum_six_distancesMem(a, position, values):
    if position == len(a) - 1:
        return a[position]
    if values[position] == -100000:
        max_forward = min(len(a) - position, 6)
        current_max = -100000
        for i in range(1, max_forward):
            local_max = max_sum_six_distancesMem(a, position + i, values)
            current_max = max(current_max, local_max)
        values[position] = current_max + a[position]
    return values[position]


def solution(A):
    values = [0] * len(A)
    values[len(A) - 1] = A[len(A) - 1]
    for i in range(len(A) - 2, -1, -1):
        values[i] = A[i] + find_max_between(values, i + 1, 6)
    return values[0]


def find_max_between(values, start, length):
    max = values[start]
    upto = min(start + length, len(values))
    for i in range(start, upto):
        if values[i] > max:
            max = values[i]
    return max


print(solutionRecursive([1, -2, 0, 9, -1, -2, 5, -4]))
print(solutionRecursive([1, -2, 0, 9, -1, -2, 5, -4, -5, -1, -10, -5, -6, -4, -2]))

print(solutionMemoize([1, -2, 0, 9, -1, -2, 5, -4]))
print(solutionMemoize([1, -2, 0, 9, -1, -2, 5, -4, -5, -1, -10, -5, -6, -4, -2]))

print(solution([1, -2, 0, 9, -1, -2, 5, -4]))
print(solution([1, -2, 0, 9, -1, -2, 5, -4, -5, -1, -10, -5, -6, -4, -2]))
