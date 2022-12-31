"""
Runtime 62 ms Beats 95.5%
Memory 14.3 MB Beats 96.21%
"""

class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        operator_funs = {
            '+': lambda x,y: x + y,
            '-': lambda x,y: x - y,
            '*': lambda x,y: x * y,
            '/': lambda x,y: x / y,
        }
        operators = ['+', '-', '*', '/']
        for token in tokens:
            if token not in operators:
                stack.append(int(token))
            else:
                if len(stack) < 2:
                    continue
                v2 = stack.pop()
                v1 = stack.pop()
                stack.append(int(operator_funs[token](v1, v2)))
        return stack[-1]

print(Solution().evalRPN(tokens = ["2","1","+","3","*"]))
print(Solution().evalRPN(tokens = ["4","13","5","/","+"]))
print(Solution().evalRPN(tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))