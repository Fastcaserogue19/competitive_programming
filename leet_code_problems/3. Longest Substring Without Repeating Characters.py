class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        char=set()
        res=0
        for i in range(len(s)):
            while s[i] in char:
                char.remove(s[l])
                l+=1
            char.add(s[i])
            res=max(res,i-l+1)
        return res
    # time complexity O(n)
    # space complexity O(n)

