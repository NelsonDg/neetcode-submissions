class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set() #make a set cause no duplicates
        l = 0
        res = 0
        for r in range(len(s)):
            while s[r] in charSet: #checking if there is a dulpicate
                charSet.remove(s[l]) #if duplicate is found remove it
                l +=1 #once removed go onto next character
            charSet.add(s[r]) #add another character on the right
            res = max(res,r - l + 1)
        return res
            
                

            