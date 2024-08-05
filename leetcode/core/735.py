# 문제를 제대로 이해 못했지만 통과된 거 보니까 왼쪽 후 오른쪽 이동은 무시하는 듯 (오른쪽 이동 기준)
# 케이스 [-2,-1,1,2] -> 답 [-2,-1,1,2]
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for a in asteroids:
            while stack and stack[-1] > 0 and a < 0:        # 오른쪽(양의 방향) 기준이기 때문에 stack[-1]이 음수인 경우는 고려하지 않음
                if stack[-1] + a < 0:
                    stack.pop()
                elif stack[-1] + a > 0:
                    break
                else:
                    stack.pop()
                    break
            else:
                stack.append(a)

        return stack

# 시간 복잡도 O(n)    while 문은 시간 복잡도에 영향을 주지 않음
# 공간 복잡도 O(n)    전체를 저장하게 될 경우

# 실패 -> 문제 이해를 못함..
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for a in asteroids:
            if not stack:
                stack.append(a)
                continue

            while stack:
                if (stack[-1] < 0 and a > 0) or (stack[-1] > 0 and a < 0):
                    if abs(stack[-1]) <= abs(a):
                        stack.pop()

                    elif abs(stack[-1]) < abs(a):
                        stack.append(a)

                    else:
                        break
                else:
                    stack.append(a)
                    break

        return stack