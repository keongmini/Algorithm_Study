def solution(numbers):
    numbers = list(map(str, numbers))

    numbers.sort(key=lambda x: x * 3, reverse=True)
    return str(int(''.join(numbers)))

s = solution([0,0,0,0])     # 엣지
print(s)