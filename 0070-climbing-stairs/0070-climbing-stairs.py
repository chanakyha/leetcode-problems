class Solution:
    def climbStairs(self, n: int) -> int:
        
        if n in [1,2]:
            return n
        
        prev = 1
        curr = 2

        for i in range(2, n):
            prev, curr = curr, curr + prev

        return curr