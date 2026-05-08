class Solution:
    def romanToInt(self, s: str) -> int:
        s = s[::-1]
        roman = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        sum = roman[s[0]]
        for i in range(1,len(s)):
            if roman[s[i-1]] <= roman[s[i]]:
                sum += roman[s[i]]
            else:
                sum -= roman[s[i]]

        return sum
        



        
        