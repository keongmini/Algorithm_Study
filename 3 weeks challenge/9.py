def solution(s):
    result = 1000
    for i in range(1, (len(s) // 2) + 1):
        prev = s[:i]
        cnt = 1

        tmp = ''

        for j in range(i, len(s), i):
            now = s[j:j + i]

            if now == prev:
                cnt += 1
            else:
                if cnt == 1:
                    tmp += prev
                else:
                    tmp += str(cnt) + prev

                prev = now
                cnt = 1

        if cnt == 1:
            tmp += prev
        else:
            tmp += str(cnt) + prev

        result = min(result, len(tmp))

    return result if result != 1000 else 1





