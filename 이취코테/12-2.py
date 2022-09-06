from collections import deque

n = input()
n_sort = deque(sorted(n))

while True:
    if not n_sort[0].isdigit():
        break
    n_sort.append(n_sort.popleft())

print(''.join(n_sort))


