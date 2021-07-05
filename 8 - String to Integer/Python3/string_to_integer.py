class Solution:
    def myAtoi(self, s: str) -> int:
        neg_or_pos = 1
        
        for i in range(len(s)):
            if s[i] != " ":
                if s[i] == "+":
                    neg_or_pos = 1
                    s = s[i+1:]
                    break
                elif s[i] == "-":
                    neg_or_pos = -1
                    s = s[i+1:]
                    break
                elif ord(s[i]) > 47 and ord(s[i]) < 58:
                    s = s[i:]
                    break
                else:
                    return 0

        num = []
        for j in range(len(s)):
            if ord(s[j]) > 47 and ord(s[j]) < 58:
                num.append(s[j])
            else:
                break
        
        if len(num) > 0:
            ans = int("".join(num))
        else:
             return 0
        
        if ans > 2**31-1 and neg_or_pos == 1:
            ans = 2**31-1
        elif ans > 2**31 and neg_or_pos == -1:
            ans = -2**31
        else:
            ans *= neg_or_pos
            
        return ans