def solution(A):
    A_abs = [abs(a) for a in A]

    return len(set(A_abs))

# 시간 복잡도 O(N) or O(N*log(N))

# https://app.codility.com/demo/results/trainingZNDQPB-N6X/