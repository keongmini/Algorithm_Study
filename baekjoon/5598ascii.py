n = input()
strList = [chr(ord(i)-3) if 67 < ord(i) < 91 else chr(ord(i)+23) for i in n ]

for i in strList:
    print(i,end="")

# ABC를 입력할 경우 XYZ로 처리