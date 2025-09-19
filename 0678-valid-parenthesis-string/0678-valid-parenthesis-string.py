class Solution:
    def checkValidString(self, s: str) -> bool:
        
        count_range = [0,0]
        for i in range(len(s)):
            if s[i] == "(":
                count_range[0] += 1
                count_range[1] += 1

            elif s[i] == ")":
                count_range[0] -= 1
                count_range[1] -= 1

            elif s[i] == "*":
                count_range[0] -= 1
                count_range[1] += 1

            if count_range[0] < 0:
                count_range[0] = 0

            if count_range[1] == -1:
                return False
            
        return count_range[0] == 0

                