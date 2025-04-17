class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        countS1 = {}
        countS2 = {}
        matches = 0

        if len(s1) > len(s2):
            return False

        for i in range(len(s1)):
            countS1[s1[i]] = 1 + countS1.get(s1[i], 0)
            countS2[s2[i]] = 1 + countS2.get(s2[i], 0)
        
        for c in "abcdefghijklmnopqrstuvwxyz":
            if c in countS1 and c in countS2 and countS1[c] == countS2[c]:
                matches += 1
            elif c not in countS1 and c not in countS2:
                matches += 1
        print (matches)
        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True
            countS2[s2[r]] = 1 + countS2.get(s2[r], 0)
            if countS2[s2[r]] == countS1.get(s2[r], 0):
                matches += 1
            elif countS2[s2[r]] - 1 == countS1.get(s2[r], 0):
                matches -= 1
            
            countS2[s2[l]] -= 1
            if countS2[s2[l]] == countS1.get(s2[l], 0):
                matches += 1
            elif countS2[s2[l]] + 1 == countS1.get(s2[l], 0):
                matches -= 1
            l += 1

        return matches == 26

        