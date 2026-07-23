class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(1, len(nums)):
            cur = nums[i]
            prev = nums[i - 1]
            if (cur == prev):
                return True
        return False
