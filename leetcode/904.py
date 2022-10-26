# 슬라이딩 윈도우 방법 2가지
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        basket = {}  # 과일나무별 등장 횟수 저장
        left = 0  # 시작점

        for right, fruit in enumerate(fruits):
            basket[fruit] = basket.get(fruit, 0) + 1  # 방문처리 - 횟수 + 1

            if len(basket) > 2:  # 두개 이상이 될 경우 시작점 이동 -> 현재 시작점 인덱스에 있는 값의 횟수 - 1
                basket[fruits[left]] -= 1

                if basket[fruits[left]] == 0:  # 횟수 없음 - 제거
                    del basket[fruits[left]]
                left += 1  # 시작점 이동

        return right - left + 1

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        basket = {}
        max_picked = 0
        left = 0

        for right in range(len(fruits)):
            basket[fruits[right]] = basket.get(fruits[right], 0) + 1

            while len(basket) > 2:
                basket[fruits[left]] -= 1
                if basket[fruits[left]] == 0:
                    del basket[fruits[left]]
                left += 1

            max_picked = max(max_picked, right - left + 1)

        return max_picked