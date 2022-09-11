# random 메소드를 이용해야만 풀리는 문제인 것 같음 
class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.cnt = nums[:]

    def reset(self) -> List[int]:
        return self.cnt

    def shuffle(self) -> List[int]:
        aux = list(self.nums)

        for i in range(len(self.nums)):
            remove_i = random.randrange(len(aux))
            self.nums[i] = aux.pop(remove_i)

        return self.nums

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()