def solution(s):
    sList = [i for i in s]

    sList.sort(reverse=True)

    return ''.join(sList)