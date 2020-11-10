# This is the solution for Arrays > OddOccurrencesInArray
#
# This is marked as PAINLESS difficulty


def solution(A):
    numbers = set([])
    for n in A:
        if n in numbers:
            numbers.discard(n)
        else:
            numbers.add(n)
    return numbers.pop()


print(solution([9, 3, 9, 3, 9, 7, 9]))

