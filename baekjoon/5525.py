# 50점
import sys

input = sys.stdin.readline

N = int(input())
M = int(input())
S = input()

P = ''
for i in range(N):
    P += 'IO'
P += 'I'


def check(string, idx):
    if string == P:
        return True

    if len(string) == len(P):
        return False

    if string[-1] != S[idx + 1]:
        return check(string + S[idx + 1], idx + 1)
    else:
        return False


result = 0

for i in range(len(S) - len(P) + 1):
    if S[i] == 'I':
        if check('I', i):
            result += 1

print(result)