class Solution:

    # This solution works for identifying strings like this : "([)]" <- In some cases, this is a valid parentheses.
    # However, in the case of this problem, this will not be good, since the parentheses need to be closed entirely
    # i.e.: the bracket between the parentheses needs to closed before we can close the parentheses..
    def isValid(self, s: str) -> bool:
        closers = [')', ']', '}']
        openers = ['(', '[', '{']
        counters = [0, 0, 0]
        for char in list(s):
            if char in closers:
                count = counters[closers.index(char)]
                if count <= 0: 
                    return False
                counters[closers.index(char)] -= 1
            else:
                counters[openers.index(char)] += 1

        return True

    """
    Runtime 38 ms Beats 74.37%
    Memory 13.8 MB Beats 71.54%
    """
    def isValid(self, s: str) -> bool:
        if len(s) < 2 or len(s) % 2 != 0: return False
        stack = []
        counterparts = {
            '(': ')', '[': ']', '{': '}',
        }

        for char in s:
            try:
                if len(stack) == 0 or counterparts[stack[-1]] != char:
                    stack.append(char)
                elif counterparts[stack[-1]] == char:
                    stack.pop()
            except:
                return False

        return True if len(stack) == 0 else False 


print(Solution().isValid(s = "()"))
print(Solution().isValid(s = "()[]{}"))
print(Solution().isValid(s = "(()())"))
print(Solution().isValid(s = "(]"))
print(Solution().isValid(s="([)]"))