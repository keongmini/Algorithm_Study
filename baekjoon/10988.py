char = input()

flag = 1
for i in range(len(char) // 2):
    if char[i] != char[len(char) - i - 1]:
        flag = 0
        print(0)
        break

if flag:
    print(1)

