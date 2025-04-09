class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        pref = 1
        for n in range(len(nums)):
            res[n] = pref
            pref = pref * nums[n]
        post = 1
        for n in range(len(nums) - 1, -1, -1):
            res[n] = res[n] * post
            post = post * nums[n]
        return res
