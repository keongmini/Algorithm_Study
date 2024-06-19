N = int(input())

pattern = input()

head, back = pattern.split("*")
length = len(head) + len(back)

for _ in range(N):
    file = input()
    flag = True

    if len(file) < length:              # 문자열 길이 고려 해야 함 -> 별표 부분을 변경해야 하기 때문에 기존 값은 수정될 수 없기 때문에
        flag = False

    if not file.startswith(head) or not file.endswith(back):
        flag = False

    if flag:
        print("DA")
    else:
        print("NE")

# files = [input() for _ in range(N)]
#
# head, back = pattern.split("*")
# back = back[::-1]
#
# for file in files:
#     flag = True
#     length = len(file)
#
#     for i in range(len(head)):
#         if head[i] != file[i] or length <= 0:
#             flag = False
#             break
#         length -= 1
#     for i in range(len(back)):
#         if back[i] != file[len(file) - i - 1] or length <= 0:
#             flag = False
#             break
#         length -= 1
#
#     if flag:
#         print("DA")
#     else:
#         print("NE")