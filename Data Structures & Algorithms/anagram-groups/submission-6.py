class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        
        for i in range(len(strs)):
            sortedWord = ''.join(sorted(strs[i]))

            if sortedWord not in d:
                d[sortedWord] = []
                d[sortedWord].append(strs[i])
            else:
                d[sortedWord].append(strs[i])

        return list(d.values())