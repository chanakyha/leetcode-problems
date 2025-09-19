class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if n == 0:
            return 0
        if n == 1:
            return 1

        left, right = 0,0
        checked = set()
        maxi = float("-inf")
        while(right<n):
            
            if s[right] not in checked:
                checked.add(s[right])
                right += 1
            else:
                checked.remove(s[left])
                left += 1

            maxi = max(len(checked), maxi)

        return maxi



        


