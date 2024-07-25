alpha = {
    "A": 3, "B": 2, "C": 1, "D": 2, "E": 3, "F": 3, "G": 3, "H": 3,
    "I": 1, "J": 1, "K": 3, "L": 1, "M": 3, "N": 3, "O": 1, "P": 2,
    "Q": 2, "R": 2, "S": 1, "T": 2, "U": 1, "V": 1, "W": 2, "X": 2, "Y": 2, "Z": 1
}

S = input()
nums = []

for s in S:
    nums.append(alpha[s])

while len(nums) > 1:
    new = []
    for i in range(0, len(nums), 2):
        if i == len(nums) - 1:
            new.append(nums[i])
            break
        now = (nums[i] + nums[i + 1]) % 10
        new.append(now)
    nums = new

if nums[0] % 2 == 0:
    print("You're the winner?")
else:
    print("I'm a winner!")