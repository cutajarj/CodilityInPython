from math import ceil, sqrt


def solution(A):
    peaks = [False] * len(A)
    for i in range(1, len(A) - 1):
        if A[i - 1] < A[i] and A[i + 1] < A[i]:
            peaks[i] = True

    upper_guess = ceil(sqrt(len(A))) + 1
    lower_guess = 0

    while lower_guess < upper_guess - 1:
        current_guess = int((lower_guess + upper_guess) / 2)
        if can_place_flags(peaks, current_guess):
            lower_guess = current_guess
        else:
            upper_guess = current_guess

    return lower_guess


def can_place_flags(peaks, flags_to_place):
    current_position = 0
    total_flags = flags_to_place
    while current_position < len(peaks) - 1 and total_flags > 0:
        if peaks[current_position]:
            total_flags -= 1
            current_position += flags_to_place
        else:
            current_position += 1
    return total_flags == 0


test_trail = [0] * 100000
for i in range(100000):
    if i % 2 == 1:
        test_trail[i] += 1

print(solution(test_trail))

