
#!O(M*N) time and space
#only lenght
class Solution: 
    def LIS(self, text1, text2):
        
        m, n = len(text1), len(text2)

        dp = [[0] * (n + 1) for _ in range(m + 1)] #(M + 1)X(N + 1) so that first row and first col are fixed at 0

        for i in range (1, m + 1):
            for j in range (1, n + 1):

                if text1[i -1] == text2[j -1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1] #the diagonal tracks the longest match until the char R of text1 and C of text2
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        
        return dp[m][n] #we want the final best LCS


#!O(M*N) time and and O(min(M,N) space
#only lenght --> we overwrite rows --> we cannot bactrack to reconstruct LCS
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # 1. Guarantee that text2 is the shorter string to optimize space
        if len(text1) < len(text2):
            text1, text2 = text2, text1
            
        m, n = len(text1), len(text2)
        
        # 2. We only need two 1D arrays of size (n + 1) --> MAXIMUM MATCH
        prev_row = [0] * (n + 1) #!RIGA PRECEDENTE in DP
        curr_row = [0] * (n + 1) #!RIGA CORRENTE in DP
        
        # 3. Fill the arrays
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    #! Characters match: look at the top-left diagonal equivalent
                    curr_row[j] = 1 + prev_row[j - 1]
                else:
                    #! Characters don't match: take max of top (prev_row) or left (curr_row)
                    curr_row[j] = max(prev_row[j], curr_row[j - 1])
            
            # 4. Move the current row to the previous row for the next iteration
            # We use a fast variable swap in Python
            prev_row, curr_row = curr_row, prev_row
            
        # Because we swap at the end of every outer loop, the final answer 
        # ends up resting inside prev_row, not curr_row.
        return prev_row[n]

#!O(M*N) time and space
#with reconstruction
def lcs_with_path(text1: str, text2: str):
    m, n = len(text1), len(text2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # --- 1. Build the DP table ---
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i - 1] == text2[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # --- 2. Reconstruct the sequence ---
    i, j = m, n
    lcs_chars = []

    # Start from the bottom-right corner and backtrack
    while i > 0 and j > 0:
        if text1[i - 1] == text2[j - 1]:
            # If characters match, it's part of the LCS
            lcs_chars.append(text1[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            # If the value above is greater, move up --> streak comes from TEXT1
            i -= 1
        else:
            # Otherwise, move left --> streak comes from TEXT2
            j -= 1

    # Since we backtracked from the end, reverse the list to get the correct order
    lcs_chars.reverse()
    result_str = "".join(lcs_chars)

    print(f"The Longest Common Subsequence is '{result_str}'")
    print(f"and its length is {dp[m][n]}")

    return dp[m][n], result_str

# Example usage:
# lcs_with_path("abcde", "ace") 
# Output: length 3, sequence "ace"
        