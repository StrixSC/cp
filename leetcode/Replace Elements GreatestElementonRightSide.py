class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        sarr = sorted([[arr[i], i] for i in range(len(arr))], key=lambda x: x[0], reverse=True)
        for i in range(len(arr) - 1):
            for entry in sarr:
                if entry[1] > i:
                    arr[i] = entry[0]
                    break
        arr[-1] = -1
        return arr
        
