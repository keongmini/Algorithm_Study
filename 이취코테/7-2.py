# 이진탐색 풀이
def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2

        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1

    return None

items_num = int(input())
items_list = list(map(int, input().split()))
items_list.sort()

order_num = int(input())
order_list = list(map(int, input().split()))
order_list.sort()

for order in order_list:
    if binary_search(items_list, order, 0, items_num - 1):
        print('yes', end=" ")
    else:
        print('no', end=" ")


# 계수정렬 풀이
n = int(input())
array = [0] * 1000001

for i in input().split():
    array[int(i)] = 1

m = int(input())
x = list(map(int, input().split()))

for i in x:
    if array[i] == 1:
        print('yes', end=" ")
    else:
        print('no', end=" ")


# 집합 자료형 풀이
n = int(input())
array = set(map(int, input().split()))

m = int(input())
x = list(map(int, input().split()))

for i in x:
    if i in array:
        print('yes', end=" ")
    else:
        print('no', end=" ")