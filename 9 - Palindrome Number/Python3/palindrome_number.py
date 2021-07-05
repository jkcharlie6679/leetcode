class Solution:
    def isPalindrome(self, x: int) -> bool:
        # return str(x) == (str(x)[::-1])
    
        if x < 0:
            return 0
        
        s = str(x)
        l = len(s)
        
        for i in range(l//2):
            if s[l -1 -i] != s[i]:
                return 0
        return 1


