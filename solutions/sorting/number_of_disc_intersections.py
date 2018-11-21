# This is the solution for Sorting > NumberOfDiscIntersections
#
# This is marked as RESPECTABLE difficulty

class Disk():
    def __init__(self, low_x, high_x):
        self.low_x = low_x
        self.high_x = high_x

def index_less_than(sortedDiskList, i, start, last):
    mid = start + (last - start) // 2
    if last <= start and sortedDiskList[mid].low_x > i:
        return mid - 1
    elif last <= start:
        return mid
    elif sortedDiskList[mid].low_x > i:
        return index_less_than(sortedDiskList, i, start, mid - 1)
    else:
        return index_less_than(sortedDiskList, i, mid + 1, last)

def solution(A):
    disks = []
    for i in range(len(A)):
        disks.append(Disk(i - A[i], i + A[i]))
    disks = sorted(disks, key=lambda d: d.low_x)
    total = 0
    for i in range(len(disks)):
        total += index_less_than(disks, disks[i].high_x + 0.5, 0, len(disks) - 1) - i
        if total > 10000000:
            total = -1
            break
    return total

print(solution([1, 5, 2, 1, 4, 0]))

print(solution([0] * 100000))