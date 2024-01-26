# 576. Out of Boundary Paths
# Medium
# Topics
# Companies
# Hint
# There is an m x n grid with a ball. The ball is initially at the position [startRow, startColumn]. You are allowed to move the ball to one of the four adjacent cells in the grid (possibly out of the grid crossing the grid boundary). You can apply at most maxMove moves to the ball.

# Given the five integers m, n, maxMove, startRow, startColumn, return the number of paths to move the ball out of the grid boundary. Since the answer can be very large, return it modulo 109 + 7.

 

# Example 1:


# Input: m = 2, n = 2, maxMove = 2, startRow = 0, startColumn = 0
# Output: 6
# Example 2:


# Input: m = 1, n = 3, maxMove = 3, startRow = 0, startColumn = 1
# Output: 12


class Solution:
    def findPaths(self, n: int, m: int, maxMove: int, startRow: int, startColumn: int) -> int:
        def F(i,j,step):
            if step>maxMove:
                return 0
            if i<0 or i>=n or j<0 or j>=m:
                if step<=maxMove:
                    return 1
                return 0
            if dp[i][j][step]!=-1:
                return dp[i][j][step]
            left=F(i,j-1,step+1)
            right=F(i,j+1,step+1)
            down=F(i+1,j,step+1)
            up=F(i-1,j,step+1)
            dp[i][j][step]=left+right+up+down
            return (left+right+down+up)
        dp=[[[-1 for _ in range(maxMove+1)] for _ in range(m+1)] for _ in range(n+1)]
        return F(startRow,startColumn,0)%((10**9)+7)