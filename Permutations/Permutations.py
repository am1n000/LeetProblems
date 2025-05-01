class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []
        lenNums = len(nums)

        def backtrack():
            if len(subset) == lenNums:
                res.append(subset[:])
                return
            for i in nums:
                if i not in subset:
                    subset.append(i)
                    backtrack()
                    subset.pop()
        
        backtrack()
        return res