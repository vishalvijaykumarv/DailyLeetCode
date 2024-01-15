# 2225. Find Players With Zero or One Losses
# Solved
# Medium
# Topics
# Companies
# Hint
# You are given an integer array matches where matches[i] = [winneri, loseri] indicates that the player winneri defeated player loseri in a match.

# Return a list answer of size 2 where:

# answer[0] is a list of all players that have not lost any matches.
# answer[1] is a list of all players that have lost exactly one match.
# The values in the two lists should be returned in increasing order.

# Note:

# You should only consider the players that have played at least one match.
# The testcases will be generated such that no two matches will have the same outcome.
 

# Example 1:

# Input: matches = [[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]
# Output: [[1,2,10],[4,5,7,8]]
# Explanation:
# Players 1, 2, and 10 have not lost any matches.
# Players 4, 5, 7, and 8 each have lost one match.
# Players 3, 6, and 9 each have lost two matches.
# Thus, answer[0] = [1,2,10] and answer[1] = [4,5,7,8].
# Example 2:

# Input: matches = [[2,3],[1,3],[5,4],[6,4]]
# Output: [[1,2,5,6],[]]
# Explanation:
# Players 1, 2, 5, and 6 have not lost any matches.
# Players 3 and 4 each have lost two matches.
# Thus, answer[0] = [1,2,5,6] and answer[1] = [].
 
class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        # Dictionary to store the number of losses for each player
        losses_count = {}

        # Iterate through matches and update losses_count
        for match in matches:
            winner, loser = match
            losses_count[loser] = losses_count.get(loser, 0) + 1
            losses_count[winner] = losses_count.get(winner, 0)

        # Create lists for players with zero losses and one loss
        zero_losses = [player for player, losses in losses_count.items() if losses == 0]
        one_loss = [player for player, losses in losses_count.items() if losses == 1]

        # Sort the lists in increasing order
        zero_losses.sort()
        one_loss.sort()

        # Return the result as a list of lists
        return [zero_losses, one_loss]