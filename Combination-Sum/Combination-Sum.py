class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        canLen = len(candidates)
        
        def dfs(i, cur, total):
            if i >= canLen or total >= target:
                if total == target:
                    res.append(cur.copy())
                return
            total += candidates[i]
            cur.append(candidates[i])
            dfs(i, cur, total)

            total -= candidates[i]
            cur.pop()
            dfs(i + 1, cur, total)
        
        dfs(0, [], 0)
        return res

