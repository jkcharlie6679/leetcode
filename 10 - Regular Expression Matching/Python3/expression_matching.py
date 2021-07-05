class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        ln_s = len(s) - 1
        ln_p = len(p) - 1
        shift = 0
        for i in range(ln_p, -1, -1):
            i -= shift
            if i < 0:
                break
            if p[i] == "*":
                if p[i-1] != ".":
                    while s[ln_s] == p[i-1]:
                        ln_s -= 1
                        if ln_s < 0:
                            break
                    shift += 1
                else:
                    if i > 1:
                        pass
                    else:
                        return 1
            elif p[i] == ".":
                if ln_s < 0:
                    return 0
                ln_s -= 1
            else:
                if ln_s < 0:
                    return 0
                if s[ln_s] == p[i]:
                    ln_s -= 1
                else:
                    return 0
        if ln_s < 0:
            return 1
        else: 
            return 0