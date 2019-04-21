# This is the solution for Prime And Composite > Flags
#
# This is marked as RESPECTABLE difficulty


def solution(A):
    peaks = [0] * len(A)
    next_peak = len(A)
    peaks[len(A) - 1] = next_peak
    for i in range(len(A) - 2, 0, -1):
        if A[i - 1] < A[i] and A[i + 1] < A[i]:
            next_peak = i
        peaks[i] = next_peak
    peaks[0] = next_peak

    current_guess = 0
    next_guess = 0
    while can_place_flags(peaks, next_guess):
        current_guess = next_guess
        next_guess += 1
    return current_guess


def can_place_flags(peaks, flags_to_place):
    current_position = 1 - flags_to_place
    for i in range(flags_to_place):
        if current_position + flags_to_place > len(peaks) - 1:
            return False
        current_position = peaks[current_position + flags_to_place]
    return current_position < len(peaks)


test_trail = [1,5,3,4,3,4,1,2,3,4,6,2]
print(solution(test_trail))

