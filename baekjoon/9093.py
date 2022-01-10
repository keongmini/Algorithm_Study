n = int(input())

for i in range(n):
    wordList = input().split()
    answer = [''.join(reversed(word)) for word in wordList]
    print(' '.join(answer))