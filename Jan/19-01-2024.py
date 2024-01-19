# 931. Minimum Falling Path Sum
# Solved
# Medium
# Topics
# Companies
# Given an n x n array of integers matrix, return the minimum sum of any falling path through matrix.

# A falling path starts at any element in the first row and chooses the element in the next row that is either directly below or diagonally left/right. Specifically, the next element from position (row, col) will be (row + 1, col - 1), (row + 1, col), or (row + 1, col + 1).

 

# Example 1:


# Input: matrix = [[2,1,3],[6,5,4],[7,8,9]]
# Output: 13
# Explanation: There are two falling paths with a minimum sum as shown.
# Example 2:


# Input: matrix = [[-19,57],[-40,-5]]
# Output: -59
# Explanation: The falling path with a minimum sum is shown.


class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        dp = matrix[0]
        for i in range(1, len(matrix)):
            dp = [
                min(
                    dp[j - 1] if j > 0 else float("Inf"),
                    dp[j],
                    dp[j + 1] if j + 1 < len(dp) else float("Inf"),
                )
                + v
                for j, v in enumerate(matrix[i])
            ]
        return min(dp)
        