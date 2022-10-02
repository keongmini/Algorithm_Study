def solution(s):
    nums = [0 for _ in range((len(s) // 2) + 1)]

    for i in range(1, len(nums)):
        save = s[:i]
        cnt = 1

        j = i
        while j < len(s):
            if save == s[j: j + i]:
                cnt += 1
            else:
                if cnt == 1:
                    nums[i] += len(save)
                else:
                    nums[i] += len(str(cnt) + save)

                save = s[j: j + i]
                cnt = 1

            if j + i >= len(s):
                if cnt == 1:
                    nums[i] += len(save)
                else:
                    nums[i] += len(str(cnt) + save)

            j += i

    return min(nums[1:])

s = solution("xababcdcdababcdcd")
print(s)