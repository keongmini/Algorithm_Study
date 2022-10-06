# 참고 https://smecsm.tistory.com/227
def solution(A):
    right_dict = {}
    for i in range(len(A)):
        if A[i] in right_dict:
            right_dict[A[i]] += 1
        else:
            right_dict[A[i]] = 1
    right_len = len(A)

    left_dict = {}
    left_max = 0
    left_max_count = 0
    left_len = 0

    cnt = 0
    for i in range(len(A)):

        right_len -= 1
        right_dict[A[i]] -= 1

        if A[i] in left_dict:
            left_dict[A[i]] += 1
        else:
            left_dict[A[i]] = 1

        left_len += 1

        if left_dict[A[i]] > left_max_count:
            left_max = A[i]
            left_max_count = left_dict[A[i]]

        if left_max_count > left_len / 2 and right_dict[left_max] > right_len / 2:      # 왼쪽에서 max인 값이 오른쪽에서 max이고 둘다 반 이상일 때만 증가
            cnt += 1

    return cnt

# 시간복잡도 O(N)

# https://app.codility.com/demo/results/training3Q5K9S-QRE/