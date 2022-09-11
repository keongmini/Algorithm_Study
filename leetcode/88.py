class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        # nums1 = nums1[:m]
        # nums1.extend(nums2)
        # nums1.sort()
        # 위 풀이 안됨

        for i in range(m, len(nums1)):
            nums1[i] = nums2[i - m]

        nums1.sort()



