class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        t = [0, 0] 

        for i in range(len(nums)):
            if t[0] != nums[i]:
                if t[1] == 0:
                    t[0] = nums[i]
                    t[1] = 1
                t[1] -= 1
            else:
                t[1] += 1

        return t[0]