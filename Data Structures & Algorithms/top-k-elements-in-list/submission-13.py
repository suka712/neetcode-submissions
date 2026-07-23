class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}

        for i in range(len(nums)):
            if nums[i] not in d:
                d[nums[i]] = 1
            else:
                d[nums[i]] = d[nums[i]] + 1
        
        s = sorted(d.items(), key = lambda x: x[1], reverse=True)

        arr = []        
        for i in range(k):
            arr.append(s[i][0])
        return arr


