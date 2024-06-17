# Bulls and Cows
# 비밀 숫자가 있음 (maybe 최대 4자리수 숫자)
# 예상되는 숫자와 비밀 숫자를 비교 했을 때, 숫자의 위치와 값 모두 일치하는 개수 Bulls, 위치는 다르지만 값이 존재하는 개수 Cows
# 힌트 형식: xAyB -> x: Bulls 개수 / y: Cows 개수

class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        x, y = 0, 0

        guess_nums = [0 for _ in range(10)]
        for i in guess:
            guess_nums[int(i)] += 1

        secret_nums = [0 for _ in range(10)]
        for i in secret:
            secret_nums[int(i)] += 1

        for i in range(len(secret)):
            now = int(secret[i])

            if now == int(guess[i]):
                x += 1
                guess_nums[now] -= 1
            elif secret_nums[now] <= guess_nums[now]:
                y += 1
                guess_nums[now] -= 1

            secret_nums[now] -= 1

        return str(x) + "A" + str(y) + "B"

s = Solution()
result = s.getHint("1123", "0111")
print(result)

# 시간 복잡도 O(n)
# 공간 복잡도 O(10) or O(1)