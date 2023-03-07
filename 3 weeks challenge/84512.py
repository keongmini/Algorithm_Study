from itertools import product   # 데카르트의 곱 (모든 경우의 수의 쌍)

def solution(word):
    words = []

    for i in range(1, 6):
        for p in product(['A', 'E', 'I', 'O', 'U'], repeat=i):
            words.append(''.join(list(p)))

    words.sort()

    return words.index(word) + 1