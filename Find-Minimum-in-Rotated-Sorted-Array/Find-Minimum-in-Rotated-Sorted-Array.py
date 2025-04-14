class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        res = nums[0]
        if nums[0] < nums[-1]:
            return nums[0]
        while l <= r:
            m = (l + r) // 2
            res = min(res, nums[m])
            if nums[m] >= nums[l]:
                res = min(res, nums[l])
                l = m + 1
            else:
                res = min(res, nums[l])
                r = m - 1
        return res
