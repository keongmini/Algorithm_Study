# 내풀이 - 실패 후 수정 - 케이스 5번 런타임에러
def solution(s):
    length = len(s) // 2
    answer = []
    for i in range(1, length + 1):
        front = s[:i]
        cnt = 1
        result = []
        for idx in range(i, len(s), i):
            if s[idx: idx + i] == front:
                cnt += 1
            else:
                if cnt == 1:
                    result.append(front)
                else:
                    result.append(str(cnt) + front)
                cnt = 1
                front = s[idx: idx + i]

        if cnt == 1:
            result.append(front)
        else:
            result.append(str(cnt) + front)
        answer.append(len(''.join(result)))
    return min(answer)

s = solution("abcabcabcabcdededededede")
print(s)

# 책풀이
def solution(s):
    answer = len(s)
    for step in range(1, len(s) // 2 + 1):
        compressed = ""
        prev = s[0:step]
        count = 1

        for j in range(step, len(s), step):
            if prev == s[j:j + step]:
                count += 1
            else:
                compressed += str(count) + prev if count >= 2 else prev
                prev = s[j:j + step]
                count = 1

        compressed += str(count) + prev if count >= 2 else prev
        answer = min(answer, len(compressed))
    return answer

s = solution("aabbaccc")
print(s)
