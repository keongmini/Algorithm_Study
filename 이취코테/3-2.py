# input 처리
n, m, k = map(int, input().split())
nums = list(map(int, input().split()))

# 리스트 큰 수 부터 배열
nums.sort(reverse=True)

max1 = nums[0]
max2 = nums[1]


# # 1. 단순 풀이
# result = 0
#
# while True:
#     for i in range(k):
#         if m == 0:
#             break
#         result += max1
#         m -= 1
#
#     if m == 0:
#         break
#     result += max2
#     m -= 1
#
# print(result)


# 2. 효율적인 풀이
#  가장 큰수 3번 + 그 다음으로 큰 수 1번 -> 4개가 반복되면됨 -> 나머지 숫자 필요x

# 가장 큰 수 더하는 갯수 구하기
cnt = int(m / (k+1)) * k
cnt += m % (k+1)

result = 0
result += cnt * max1
result += (m-cnt) * max2

print(result)


