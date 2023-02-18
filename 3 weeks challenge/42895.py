import collections


def solution(N, number):
    if N == number:
        return 1

    nums = collections.defaultdict(set)

    for idx in range(1, 9):
        nums[idx].add(int(str(N) * idx))

        for i in range(1, idx):
            for num1 in nums[i]:
                for num2 in nums[idx - i]:
                    nums[idx].add(num1 * num2)
                    nums[idx].add(num1 + num2)
                    nums[idx].add(num1 - num2)
                    if num2 != 0:
                        nums[idx].add(num1 // num2)

        if number in nums[idx]:
            return idx

    return -1


