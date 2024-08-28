class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        num = sorted(nums)
        dlina = len(nums)
        x = max(nums)
        for i in range(dlina - 1):
            if (num[i] * 2) > x:
                return -1
        return nums.index(x)
