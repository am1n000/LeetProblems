class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ordNums = set(nums)
        longest = 0

        for n in ordNums:
            if (n - 1) not in ordNums:
                length = 0
                while (n + length) in ordNums:
                    length += 1
                longest = max(longest, length)
        return longest