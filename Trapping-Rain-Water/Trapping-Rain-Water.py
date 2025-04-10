class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        l = 0
        r = len(height) - 1
        maxL = 0
        maxR = 0

        while l <= r:
            if maxL <= maxR:
                res += max(0, maxL - height[l])
                maxL = max(height[l], maxL)
                l += 1
            else:
                res += max(0, maxR - height[r])
                maxR = max(height[r], maxR)
                r -= 1
        return res

