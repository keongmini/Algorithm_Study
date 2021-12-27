word = input()

alphabet = [chr(i) for i in range(97, 123)]

for i in range(len(alphabet)):
    if alphabet[i] in word:
        alphabet[i] = word.index(alphabet[i])
    else:
        alphabet[i] = -1

for i in alphabet:
    print(i, end=" ")

# 참고
# find 함수
# word.find('a') -> 1