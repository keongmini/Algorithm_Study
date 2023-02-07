# def solution(name):
#     front = ord('A')
#     back = ord('Z') + 1
#
#     cnt = len(name) - name.count('A')
#     now1 = 0
#     for i in range(len(name)):
#         char = name[i]
#
#         if cnt == 0:
#             break
#
#         if i > 0:
#             now1 += 1  # 다음 글자로 이동
#
#         if char == 'A':
#             continue
#
#         now1 += min(ord(char) - front, back - ord(char))
#         cnt -= 1
#
#     cnt = len(name) - name.count('A')
#     now2 = 0
#     for i in range(len(name) - 1, -1, -1):
#         char = name[i]
#
#         if cnt == 0:
#             break
#
#         if char == 'A':
#             continue
#
#         now2 += min(ord(char) - front, back - ord(char))
#         cnt -= 1
#
#     return min(now1, now2)

def solution(name):
    front = ord('A')
    back = ord('Z') + 1

    cnt = len(name) - name.count('A')

    result = 0
    for i in range(len(name)):
        char = name[i]

        if cnt == 0:
            break

        result += 1  # 다음 글자로 이동

        if char != 'A':
            result += min(ord(char) - front, back - ord(char))
            cnt -= 1

    result -= 1  # 첫 글자 이동 x
