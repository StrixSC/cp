class Solution:
    def romanToInt(self, s: str) -> int:
        slist = list(s)
        slist.reverse()
        values = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        res = 0
        while len(slist) != 0:
            val = slist.pop()
            if len(slist):
                lookahead = slist[-1]
            else: lookahead = 0

            if val is "I" and lookahead:
                if lookahead is "V":
                    res += 4
                    slist.pop()
                elif lookahead is "X":
                    res += 9
                    slist.pop()
                else:
                    res += values[val]
            elif val is "X" and lookahead:
                if lookahead is "L":
                    res += 40
                    slist.pop()
                elif lookahead is "C":
                    res += 90
                    slist.pop()
                else:
                    res += values[val]
            elif val is "C" and lookahead:
                if lookahead is "D":
                    res += 400
                    slist.pop()
                elif lookahead is "M":
                    res += 900
                    slist.pop()
                else:
                    res += values[val]
            else:
                res += values[val]

        return res
