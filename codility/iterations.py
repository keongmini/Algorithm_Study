def solution(N):
    bin = format(N, 'b')

    bin = str(int(bin))

    if bin.count('1') <= 1 or bin.count('1') == len(bin):
        return 0

    idx = [i for i in range(len(bin)) if bin[i] == '1']

    result = 0
    for i in range(len(idx) - 1):
        result = max(idx[i + 1] - idx[i], result)

    return result - 1

# https://app.codility.com/demo/results/trainingCQ2CJJ-VHR/