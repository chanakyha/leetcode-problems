class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        S, T = len(s), len(t)

        if S > T: return False
        if s == "" : return True

        j = 0


        for i in range(T):
            if s[j] == t[i]:
                if j == S - 1:
                    return True
                j += 1
        return False 
        