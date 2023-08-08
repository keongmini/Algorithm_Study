N = int(input())

alpha = {}          # 각 알파벳별 존재하는 자리 저장(해당 자리에 없으면 0 있으면 1 이상 - 다른 문자열 같은 자릿수에 같은 알파벳이 있을 수 있으니까)

for _ in range(N):
    string = input()
    length = len(string) - 1            # 존재하는지 자릿수

    for i in range(len(string)):
        if string[i] in alpha:
            alpha[string[i]] += 10 ** length        # 원래 있으면 누적해서 자리 업데이트
        else:
            alpha[string[i]] = 10 ** length

        length -= 1

nums = list(alpha.values())
nums.sort(reverse=True)     # 내림차순으로 정렬하게 되면 가장 첫번째 자리에 있어야 할 값이 처음에 옴

result = 0

cnt = 9

for num in nums:
    result += num * cnt
    cnt -= 1

print(result)