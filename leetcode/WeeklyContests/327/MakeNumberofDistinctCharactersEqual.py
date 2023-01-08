class Solution:
    def getDistinctCharacterCount(self, s):
        return len(set(s))

    def isItPossible(self, word1: str, word2: str) -> bool:
        for i in range(len(word1)):
            for j in range(len(word2)):
                tmp1 = list(word1)
                tmp2 = list(word2)
                tmp3 = ""
                tmp3 = tmp1[i]
                tmp1[i] = tmp2[j]
                tmp2[j] = tmp3
                if len(set(tmp1)) == len(set(tmp2)):
                    return True

        return False 

print(Solution().isItPossible( word1 = "aa", word2 = "bb"))
print(Solution().isItPossible( word1 = "ac", word2 = "b"))
print(Solution().isItPossible(word1 = "abcc", word2 = "aab"))