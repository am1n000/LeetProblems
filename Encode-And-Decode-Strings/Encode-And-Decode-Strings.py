class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += s + chr(31)
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        word = ""
        for i in s:
            if ord(i) == 31:
                res.append(word)
                word = ""
            else:
                word = word + i
        return res