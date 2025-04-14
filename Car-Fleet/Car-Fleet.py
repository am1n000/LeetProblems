class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        speed_map = {}
        
        for i, pos in enumerate(position):
            speed_map[pos] = speed[i]

        position.sort(reverse=True)
        
        for pos in position:
            t = (target - pos) / speed_map[pos]
            if stack and t <= stack[-1]:
                continue
            stack.append(t)
        return len(stack)