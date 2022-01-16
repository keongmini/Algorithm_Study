k = int(input())

for _ in range(k):
    m,n = map(int, input().split())
    numList = list(map(int, input().split()))
    idx = [[v,i] for i,v in enumerate(numList)]
    answer = []

    while idx:
        maxNum = max(idx)[0]
        if maxNum == idx[0][0]:
            answer.append(idx.pop(0))
        else:
            idx.append(idx.pop(0))

    for i in answer:
        if i[1] == n:
            a = answer.index(i)
            print(a+1)
            break