class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        z = list(zip(s, t))
        print(z)

        for i in range(len(z) - 1, 0, -1):
            if z[i][0] == z[i][1]:
                res = i
                
                


print(Solution().appendCharacters(s = "coaching", t = "coding"))
# print(Solution().appendCharacters(s = "abcde", t = "a"))
# print(Solution().appendCharacters(s = "zen", t = "abcde"))
# print(Solution().appendCharacters(s = "a", t = "a"))
# print(Solution().appendCharacters(s = "azbc", t = "abzc"))