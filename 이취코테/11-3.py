# # 내 풀이
# nums = [int(i) for i in input()]
#
# result = [0, 0]
# for i in range(len(nums) - 1):
#     if nums[i] == 0 and nums[i + 1] != 0:
#         result[0] += 1
#     elif nums[i] == 1 and nums[i + 1] != 1:
#         result[1] += 1
#
#
# if nums[len(nums) - 1] != nums[len(nums) - 2]:
#     result[nums[len(nums) - 1]] += 1
#
# print(min(result))

# 책 풀이
data = input()
count0 = 0
count1 = 0

if data[0] == '1':
    count0 += 1
else:
    count1 += 1

for i in range(len(data) - 1):
    if data[i] != data[i + 1]:
        if data[i + 1] == '1':
            count0 += 1
        else:
            count1 += 1

print(min(count0, count1))

# 내 풀이 - 앞에서부터 차례대로 그룹 짓고 개수 count + 마지막 부분 처리 (방향이 더 작은 인덱스에 향해 있음)
# 책 풀이 - 앞 부분 처리 + 앞 부분 다음부터 차례대로 count (방향이 더 큰 인덱스에 향해 있음)
