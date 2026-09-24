class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charset = set()
        l = 0
        res = 0

        for r in range(len(s)): #right pointer goes through everything and u can intialize it like this
            while s[r] in charset: #showing the its a duplicate
                charset.remove(s[l]) #removing the duplicate
                l +=1 # update left pointer
            charset.add(s[r]) # after removing duplicate add rightmost pointer
            res = max(res, r - l  + 1) 
        return res