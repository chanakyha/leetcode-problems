class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort(key=len)
        sb = []
        for i in range(len(strs[0])):
            matched = strs[0][i]
            for s in strs:
                if(s[i] != matched):
                    return "".join(sb)
            else:
                sb.append(s[i])
        
        else:
            return strs[0]