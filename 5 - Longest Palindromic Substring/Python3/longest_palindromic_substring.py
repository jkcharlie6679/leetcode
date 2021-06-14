class Solution:
    def longestPalindrome(self, s: str) -> str:
        length = len(s)
        max = 0
        output = []
        for i in range(length):
            break0 = 0
            break1 = 0
            for j in range(i+1):
                if (i+j+1 < length) and break0 == 0:
                    if (s[i-j] != s[i+j+1]):
                        if j*2 > max:
                            max = j*2
                            output = s[i-j+1:i+j+1]
                        break0 = 1
                    elif (i-j == 0) or (i+j+1) == length -1:
                        if (j+1)*2 > max:
                            max = (j+1)*2
                            output = s[i-j:i+j+2]
                        break0 = 1
                
                if (i+j < length) and break1 == 0:
                    if(s[i-j] != s[i+j]):
                        if (j - 1)*2 +1> max:
                            max = (j - 1)*2 +1
                            output = s[i-j+1:i+j]
                        break1 = 1
                    elif (i-j == 0) or (i+j) == length -1:
                        if j*2 +1> max:
                            max = j*2 +1
                            output = s[i-j:i+j+1]
                        break1 = 1
        return output

class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        n = len(s)
        # Form a bottom-up dp 2d array
        # dp[i][j] will be 'true' if the string from index i to j is a palindrome. 
        dp = [[False] * n  for a in range(n)]

        ans = ''
        # every string with one character is a palindrome
        for i in range(n):
            dp[i][i] = True
            ans = s[i]

        maxLen = 1
        for start in range(n-1, -1, -1):
            for end in range(start+1, n):             
				# palindrome condition
                if s[start] == s[end]:
                    print(start, end)
                    # if it's a two char. string or if the remaining string is a palindrome too
                    if end - start == 1 or dp[start+1][end-1]:
                        dp[start][end] = True
                        if maxLen < end - start + 1:
                            maxLen = end - start + 1
                            ans = s[start: end+ 1]
        
        return ans