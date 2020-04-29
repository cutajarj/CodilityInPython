# This is the solution for Euclidean Algorithm > Chocolate by Numbers
#
# This is marked as PAINLESS difficulty


def find_gcd(a, b):
    if b == 0:
        return a
    else:
        return find_gcd(b, a % b)


def solution(N, M):
    return N // find_gcd(N, M)


print(solution(10, 4))

print(solution(9, 6))

print(solution(10, 11))

