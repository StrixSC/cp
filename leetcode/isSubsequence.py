class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s = list(reversed(list(s)))
        for letter in list(t):
            if len(s) == 0:
                return True
            
            if letter == s[-1]:
                s.pop()

        return True if not len(s) else False