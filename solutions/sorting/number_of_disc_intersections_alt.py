# This is the solution for Sorting > NumberOfDiscIntersections
#
# This is marked as RESPECTABLE difficulty

class Disc():
    def __init__(self, low_x, high_x):
        self.low_x = low_x
        self.high_x = high_x

def index_less_than(sortedDiscList, i, start, last):
    mid = start + (last - start) // 2
    if last <= start and sortedDiscList[mid].low_x > i:
        return mid - 1
    elif last <= start:
        return mid
    elif sortedDiscList[mid].low_x > i:
        return index_less_than(sortedDiscList, i, start, mid - 1)
    else:
        return index_less_than(sortedDiscList, i, mid + 1, last)

def solution(A):
    discs = []
    for i in range(len(A)):
        discs.append(Disc(i - A[i], i + A[i]))
    discs = sorted(discs, key=lambda d: d.low_x)
    total = 0
    for i in range(len(discs)):
        total += index_less_than(discs, discs[i].high_x + 0.5, 0, len(discs) - 1) - i
        if total > 10000000:
            total = -1
            break
    return total

print(solution([1, 5, 2, 1, 4, 0]))

print(solution([0] * 100000))
