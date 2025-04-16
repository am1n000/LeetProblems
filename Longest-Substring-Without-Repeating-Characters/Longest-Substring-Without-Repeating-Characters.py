class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        arr = [-1] * 256
        index = -1
        l = 0
        for i, w in enumerate(s):
            if arr[ord(w)] > index:
                index = arr[ord(w)]
            arr[ord(w)] = i
            if l < i - index:
                l = i - index
        
        return l