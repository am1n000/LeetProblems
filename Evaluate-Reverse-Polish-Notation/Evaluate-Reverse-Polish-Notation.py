class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for t in tokens:
            if t in "+-*/":
                tmp = stack.pop()
                if t == "+":
                    stack[-1] += tmp
                elif t == "-":
                    stack[-1] -= tmp
                elif t == "*":
                    stack[-1] *= tmp
                else:
                    stack[-1] = int(stack[-1] / tmp)
            else:
                stack.append(int(t))
        return stack[-1]