# 이진탐색
def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2

        if array[mid] == target:
            return True
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1

    return None

card_num = int(input())
card_list = list(map(int, input().split()))
card_list.sort()

mycard_num = int(input())
mycard_list = list(map(int, input().split()))

for card in mycard_list:
    if binary_search(card_list, card, 0, card_num-1):
        print('1', end=" ")
    else:
        print('0', end=" ")

# 집합 자료형
import sys
card_num = int(input())
card_list = set(map(int, sys.stdin.readline().rstrip().split()))    # list로 할경우 에러 시간초과 발생

mycard_num = int(input())
mycard_list = list(map(int, sys.stdin.readline().rstrip().split()))

for card in mycard_list:
    if card in card_list:
        print('1', end=" ")
    else:
        print('0', end=" ")

# 이진탐색보다 집합자료형 풀이가 훨씬 빠름