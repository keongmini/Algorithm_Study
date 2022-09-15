class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) < len(nums2):
            check1, check2 = nums1, nums2
        else:
            check1, check2 = nums2, nums1

        result = []
        for num in check1:
            if num in check2:
                result.append(num)
                check2.remove(num)

        return result