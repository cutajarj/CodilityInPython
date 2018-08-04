class CyclicRotation:

    def solution(self, array, k):
        result = [None] * len(array)
        for i in range(len(array)):
            result[(i + k) % len(array)] = array[i]
        return result

x = [1,2,3,4,5]
print (CyclicRotation().solution(array = x, k = 2))


