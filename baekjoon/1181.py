# 삽입 정렬 - 시간초과
n = int(input())

words = []
for _ in range(n):
    words.append(input())

words = list(set(words))

for i in range(len(words)):
    for j in range(i, 0, -1):
        if len(words[j]) < len(words[j - 1]):
            words[j], words[j - 1] = words[j - 1], words[j]
        elif len(words[j]) == len(words[j - 1]) and words[j] < words[j - 1]:
            words[j], words[j - 1] = words[j - 1], words[j]
        else:
            break

for word in words:
    print(word)

# 정렬 라이브러리 사용 - 통과
n = int(input())

words = []
for _ in range(n):
    words.append(input())
words = list(set(words))

word_list = []
for word in words:
    word_list.append([len(word), word])

word_list.sort() # 앞자리 기준 정렬 후 뒷자리 기준 정렬 진행 

for word in word_list:
    print(word[1])