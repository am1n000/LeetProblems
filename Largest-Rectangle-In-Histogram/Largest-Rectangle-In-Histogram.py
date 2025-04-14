class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxArea = 0
        l = len(heights)
        for i, h in enumerate(heights):
            if stack and h < stack[-1][1]:
                last = [0, 1]
                while stack and h < stack[-1][1]:
                    last = stack.pop()
                    area = last[1] * (i - last[0])
                    if area > maxArea:
                        maxArea = area
                stack.append((last[0], h))
            else:
                stack.append((i, h))
        while stack:
            last = stack.pop()
            area = (l - last[0]) * last[1]
            if area > maxArea:
                maxArea = area
        return maxArea