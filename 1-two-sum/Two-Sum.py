class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        trac = {}
        for i, v in enumerate(nums):
            diff = target - v
            if diff in trac:
                return [trac[diff], i]
            trac[v] = i
        return
        