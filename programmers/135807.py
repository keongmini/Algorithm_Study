def check(num):
    result = []

    for i in range(1, int(num ** (1 / 2)) + 1):
        if num % i == 0:
            result.append(i)

            if i ** 2 != num:
                result.append(num // i)
    return result


def solution(arrayA, arrayB):
    arrayA.sort()
    numsA = check(arrayA[0])

    arrayB.sort()
    numsB = check(arrayB[0])

    nums = numsA + numsB
    nums = set(nums)

    result = 0
    for n in nums:
        if n in numsA and n in numsB:
            continue

        if n in numsA:
            flag = True
            for a in arrayA:
                if a % n != 0:
                    flag = False
                    break

            if flag:
                for b in arrayB:
                    if b % n == 0:
                        flag = False
                        break

            if flag:
                result = max(result, n)

        if n in numsB:
            flag = True
            for b in arrayB:
                if b % n != 0:
                    flag = False
                    break

            if flag:
                for a in arrayA:
                    if a % n == 0:
                        flag = False
                        break

            if flag:
                result = max(result, n)

    return result