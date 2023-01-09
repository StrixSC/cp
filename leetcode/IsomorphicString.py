class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t) or len(set(s)) != len(set(t)):
            return False
        dic = {}
        s = list(s)
        t = list(t)
        for i in range(len(s)):
            if s[i] in dic and dic[s[i]] != t[i]:
                return False
            else:
                dic[s[i]] = t[i]
        return True