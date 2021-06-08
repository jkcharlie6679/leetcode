class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        list = []
        max = 0
        ans = 0
        for i in range(len(s)):
            if s[i] not in list:
                max += 1
                list.append(s[i])
                if ans < max:
                    ans = max
            else:
                max -= list.index(s[i])
                list.append(s[i])
                list = list[list.index(s[i]) + 1:]
        return ans