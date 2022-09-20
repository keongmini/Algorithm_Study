def solution(lottos, win_nums):
    rate = {
        6: 1,
        5: 2,
        4: 3,
        3: 4,
        2: 5
    }
    result = [0, 0]

    for num in lottos:
        if num in win_nums:
            result[1] += 1
        elif num == 0:
            result[0] += 1

    result[0] += result[1]

    for i in range(len(result)):
        if result[i] < 2:
            result[i] = 6
        else:
            result[i] = rate[result[i]]

    return result

