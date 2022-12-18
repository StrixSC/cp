class Solution:
    # Algorithm:
    """
        Add every matrix[0][i] for i in 0..m (Top left to Top right)
        Add every matrix[i][m] for i in 0..n (Top right to bottom right)
        Add every matrix[n][i] for i in m..0 (Bottom right to bottom left)
        Add every matrix[i][0] for i in n..0 (Bottom left to top left)
        repeat until no more numbers in the array
    """

    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        r,n,m = [], len(matrix) - 1, len(matrix[0]) - 1
        seen = set()
        top, bottom, left, right = 0,0,0,0

        while len(r) < (n+1) * (m+1):
            # Add every matrix[0][i] for i in 0..m (Top left to Top right)
            i = left
            while i <= m - right:
                if (top,i) not in seen:
                    r.append(matrix[top][i])
                seen.add((top, i))
                i+=1
            top += 1

            # Add every matrix[i][m] for i in 0..n (Top right to bottom right)
            i = top
            while i <= n - bottom:
                if (i, m-right) not in seen:
                    r.append(matrix[i][m-right])
                seen.add((i, m-right))
                i+=1
            right += 1

            # Add every matrix[n][i] for i in m..0 (Bottom right to bottom left)
            i = m - right
            while i >= left:
                if (n-bottom, i) not in seen:
                    r.append(matrix[n-bottom][i])
                seen.add((n-bottom, i))
                i-=1
            bottom += 1

            # Add every matrix[i][0] for i in n..0 (Bottom left to top left)
            i = n-bottom
            while i >= top:
                if (i, left) not in seen:
                    r.append(matrix[i][left])
                seen.add((i, left))
                i-=1
            left += 1

        return r



print(Solution().spiralOrder([[1,2,3],[4,5,6],[7,8,9]]) == [1, 2, 3, 6, 9, 8, 7, 4, 5])
print(Solution().spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]) == [1,2,3,4,8,12,11,10,9,5,6,7])
