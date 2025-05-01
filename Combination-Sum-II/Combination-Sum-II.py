class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        canLen = len(candidates)
        def dfs(idx, cur, total):
            if total >= target:
                if total == target:
                    res.append(cur.copy())
                return
            for i in range(idx, canLen):
                if i > idx and candidates[i] == candidates[i - 1]:
                    continue
                if total + candidates[i] > target:
                    break
                dfs(i + 1, cur+[candidates[i]], total + candidates[i])

        candidates.sort()
        dfs (0, [], 0)
        return res
