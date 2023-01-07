class Solution:
    def valid_combination(n: int, combination: str):
        count_opened = combination.count("(")
        count_closed = combination.count(")")
        c1 = count_closed <= count_opened
        c2 = count_opened > 0
        c3 = count_opened < n
        return c1 and c2 and c3

    def generateParenthesis(self, n: int) -> list[str]:
        combinations = []
        return combinations

print(Solution().generateParenthesis(n=3))