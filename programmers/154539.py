def solution(numbers):
    result = [-1 for _ in range(len(numbers))]

    stack = []
    for i in range(len(numbers)):
        while stack and numbers[stack[-1]] < numbers[i]:
            result[stack.pop()] = numbers[i]

        stack.append(i)

    return result

