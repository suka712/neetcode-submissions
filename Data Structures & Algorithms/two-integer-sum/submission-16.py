class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        s = set(nums)

        for i in range(len(nums)):
            if target - nums[i] in s:
                for k in range(i + 1, len(nums)):
                    if nums[k] == target - nums[i]:
                        return [i, k]