# H-Index
# 논문 n편 중, h번 이상 인용된 논문이 h편 이상이고 나머지 논문이 h번 이하 인용되었다면 h의 최댓값 -> H-index
# 적어도 h번 인용된 게 적어도 h개 인 h 값중 최대값

class Solution:
    def hIndex(self, citations) -> int:
        citations.sort()

        for i, c in enumerate(citations):           # 전체 개수 = h의 최대값
            if len(citations) - i <= c:             # 전체 길이에서 작은값(i)부터 빼주기 때문에 인용이 가장 많이 된 순간 부터 구할 수 있음
                return len(citations) - i

        return 0

# 시간 복잡도 O(NlogN) 정렬의 시간복잡도가 nlogn / 반복문의 시간복잡도는 무시된 것 같다
# 공간 복잡도 O(N) 정렬 알고리즘의 대부분은 공간복잡도가 n